"""Rewrite the Loops OpenAPI spec into the input openapi-python-client can generate from.

The generator names a model after its schema's ``title`` when one is set. Loops
uses titles as display labels and repeats them ("Signup trigger" labels five
schemas), so the generator sees duplicate models, drops them, and then drops
every endpoint and response that referenced one. Without titles each model is
named after its schema key, which is unique.

The spec is read and written with the YAML loader the generator itself uses, so
the generator sees every other value exactly as it would in the original.

The shipped ``src/pyloops/openapi.yaml`` stays as fetched; only the generator
reads the normalized copy.

Usage: python scripts/normalize_spec.py <spec.yaml> <normalized.yaml>
"""

import sys
from pathlib import Path
from typing import Any

from ruamel.yaml import YAML

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
# Example payloads outside a schema: free-form, and never read as schemas.
_EXAMPLES = frozenset({"example", "examples"})


def _yaml() -> YAML:
    # typ="safe" is what openapi-python-client loads the document with. ruamel.yaml
    # is installed as that dev dependency's own requirement.
    yaml = YAML(typ="safe")
    yaml.default_flow_style = False
    # Property order becomes field order in the generated models.
    yaml.representer.sort_base_mapping_type_on_output = False
    return yaml


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
        elif key not in _EXAMPLES and not str(key).startswith("x-"):
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
    return _yaml().load(path)


def main(argv: list[str]) -> int:
    if len(argv) != 3:
        print(__doc__, file=sys.stderr)
        return 2
    source, target = Path(argv[1]), Path(argv[2])
    spec = load_spec(source)
    stripped = normalize(spec)
    _yaml().dump(spec, target)
    print(f"Stripped {stripped} schema title(s) from {source} into {target}")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
