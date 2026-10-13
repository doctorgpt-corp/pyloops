"""Rewrite the Loops OpenAPI spec into the input openapi-python-client can generate from.

The generator names a model after its schema's ``title`` when one is set. Loops
uses titles as display labels and repeats them ("Signup trigger" labels five
schemas), so the generator sees duplicate models, drops them, and then drops
every endpoint and response that referenced one. Without titles each model is
named after its schema key, which is unique.

The shipped ``src/pyloops/openapi.yaml`` stays as fetched; only the generator
reads the normalized copy.

Usage: python scripts/normalize_spec.py <spec.yaml> <normalized.json>
"""

import json
import sys
from pathlib import Path
from typing import Any

import yaml

# Keywords whose value is a map of name -> schema. The names are data, so a
# property called "title" is kept.
_SCHEMA_MAPS = frozenset({"properties", "patternProperties", "$defs", "dependentSchemas"})
_SCHEMA_LISTS = frozenset({"allOf", "anyOf", "oneOf", "prefixItems"})
_SCHEMAS = frozenset(
    {
        "items",
        "additionalProperties",
        "not",
        "if",
        "then",
        "else",
        "contains",
        "propertyNames",
        "unevaluatedItems",
        "unevaluatedProperties",
    }
)
# Free-form values that can hold a "schema" or "title" key of their own.
_OPAQUE = frozenset({"example", "examples", "default", "enum", "const"})


class _SpecLoader(yaml.SafeLoader):
    """SafeLoader that leaves timestamps as strings so the spec round-trips to JSON."""


_SpecLoader.yaml_implicit_resolvers = {
    first_char: [(tag, regexp) for tag, regexp in resolvers if tag != "tag:yaml.org,2002:timestamp"]
    for first_char, resolvers in yaml.SafeLoader.yaml_implicit_resolvers.items()
}


def _strip_schema_titles(schema: Any) -> int:
    if not isinstance(schema, dict):
        return 0
    stripped = 0
    if isinstance(schema.get("title"), str):
        del schema["title"]
        stripped += 1
    for keyword, value in schema.items():
        if keyword in _SCHEMA_MAPS and isinstance(value, dict):
            stripped += sum(_strip_schema_titles(member) for member in value.values())
        elif keyword in _SCHEMA_LISTS and isinstance(value, list):
            stripped += sum(_strip_schema_titles(member) for member in value)
        elif keyword in _SCHEMAS:
            stripped += _strip_schema_titles(value)
    return stripped


def _strip_nested_schemas(node: Any) -> int:
    """Strip titles from every ``schema`` found under parameters, bodies, responses and headers."""
    if isinstance(node, list):
        return sum(_strip_nested_schemas(member) for member in node)
    if not isinstance(node, dict):
        return 0
    stripped = 0
    for key, value in node.items():
        if key == "schema":
            stripped += _strip_schema_titles(value)
        elif key not in _OPAQUE:
            stripped += _strip_nested_schemas(value)
    return stripped


def normalize(spec: dict[str, Any]) -> int:
    """Remove every schema ``title`` from ``spec`` in place and return how many were removed."""
    components = spec.get("components", {})
    stripped = sum(_strip_schema_titles(schema) for schema in components.get("schemas", {}).values())
    stripped += _strip_nested_schemas(spec.get("paths", {}))
    stripped += _strip_nested_schemas({name: group for name, group in components.items() if name != "schemas"})
    return stripped


def load_spec(path: Path) -> dict[str, Any]:
    return yaml.load(path.read_text(), Loader=_SpecLoader)


def main(argv: list[str]) -> int:
    if len(argv) != 3:
        print(__doc__, file=sys.stderr)
        return 2
    source, target = Path(argv[1]), Path(argv[2])
    spec = load_spec(source)
    stripped = normalize(spec)
    target.write_text(json.dumps(spec, indent=2) + "\n")
    print(f"Stripped {stripped} schema title(s) from {source} into {target}")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
