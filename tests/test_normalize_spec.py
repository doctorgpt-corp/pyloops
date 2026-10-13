import copy
import importlib.util
from pathlib import Path
from typing import Any

import pyloops

SCRIPT = Path(__file__).parent.parent / "scripts" / "normalize_spec.py"

_spec = importlib.util.spec_from_file_location("normalize_spec", SCRIPT)
assert _spec and _spec.loader
normalize_spec = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(normalize_spec)


def _title_paths(node: Any, path: tuple[str, ...] = ()) -> list[tuple[str, ...]]:
    """Every place a string ``title`` sits, found without knowing what a schema is."""
    if isinstance(node, list):
        return [found for index, member in enumerate(node) for found in _title_paths(member, (*path, str(index)))]
    if not isinstance(node, dict):
        return []
    found = [path] if isinstance(node.get("title"), str) else []
    for key, value in node.items():
        found += _title_paths(value, (*path, str(key)))
    return found


def _ordered(node: Any) -> Any:
    """``node`` with every mapping as a list of pairs, so comparing it compares key order too."""
    if isinstance(node, dict):
        return [(key, _ordered(value)) for key, value in node.items()]
    if isinstance(node, list):
        return [_ordered(member) for member in node]
    return node


def test_strips_titles_from_component_schemas_at_any_depth():
    spec = {
        "components": {
            "schemas": {
                "Node": {
                    "title": "Signup trigger",
                    "type": "object",
                    "properties": {"value": {"oneOf": [{"title": "String", "type": "string"}]}},
                    "additionalProperties": {"anyOf": [{"title": "Number", "type": "number"}]},
                    "allOf": [{"title": "Identify by email", "required": ["email"]}],
                    "items": {"title": "Item", "type": "string"},
                }
            }
        }
    }

    assert normalize_spec.normalize(spec) == 5
    assert _title_paths(spec) == []


def test_strips_titles_from_schemas_inlined_in_paths_and_components():
    body = {"content": {"application/json": {"schema": {"title": "Body", "type": "object"}}}}
    spec = {
        "paths": {
            "/v1/things": {
                "post": {
                    "parameters": [{"name": "q", "in": "query", "schema": {"title": "Query", "type": "string"}}],
                    "requestBody": copy.deepcopy(body),
                    "responses": {"200": copy.deepcopy(body), "default": copy.deepcopy(body)},
                }
            }
        },
        "components": {
            "requestBodies": {"default": copy.deepcopy(body)},
            "responses": {"NotFound": copy.deepcopy(body)},
        },
    }

    assert normalize_spec.normalize(spec) == 6
    assert _title_paths(spec) == []


def test_keeps_titles_that_do_not_name_a_schema():
    spec = {
        "info": {"title": "Loops OpenAPI Spec"},
        "paths": {
            "/v1/things": {
                "get": {
                    "x-mint": {"metadata": {"title": "List things"}, "schema": {"title": "Not a schema"}},
                    "responses": {
                        "200": {
                            "content": {
                                "application/json": {
                                    "example": {"schema": {"title": "Payload"}},
                                    "examples": {"one": {"value": {"schema": {"title": "Payload"}}}},
                                }
                            }
                        }
                    },
                }
            }
        },
        "components": {
            "schemas": {
                "Rule": {
                    "type": "object",
                    "properties": {"title": {"type": "string"}},
                    "required": ["title"],
                    "example": {"title": "Missing button link"},
                    "examples": [{"title": "Missing text link"}],
                    "default": {"title": "Untitled"},
                    "enum": [{"title": "One"}],
                    "const": {"title": "Only"},
                }
            }
        },
    }
    untouched = copy.deepcopy(spec)

    assert normalize_spec.normalize(spec) == 0
    assert spec == untouched


def test_generator_reads_every_other_value_unchanged(tmp_path):
    # Scalars PyYAML and JSON would each read differently from the generator's loader.
    source = tmp_path / "spec.yaml"
    source.write_text(
        "components:\n"
        "  schemas:\n"
        "    Thing:\n"
        "      title: Thing label\n"
        "      required: [zebra, apple]\n"
        "      properties:\n"
        "        zebra: {type: string}\n"
        "        apple: {type: string}\n"
        "      enum:\n"
        "        - on\n"
        "        - yes\n"
        "        - 0123\n"
        "        - 1e3\n"
        "        - 2026-01-02T03:04:05Z\n"
        "        - '2026-01-02'\n"
        "        - null\n"
        "        - 1.5\n"
    )
    target = tmp_path / "normalized.yaml"
    expected = normalize_spec.load_spec(source)
    del expected["components"]["schemas"]["Thing"]["title"]

    assert normalize_spec.main(["normalize_spec", str(source), str(target)]) == 0

    assert _ordered(normalize_spec.load_spec(target)) == _ordered(expected)


def test_shipped_spec_loses_only_its_schema_titles(tmp_path):
    source = pyloops.openapi_spec_path()
    target = tmp_path / "normalized.yaml"
    expected = normalize_spec.load_spec(source)
    stripped = normalize_spec.normalize(expected)

    assert normalize_spec.main(["normalize_spec", str(source), str(target)]) == 0

    normalized = normalize_spec.load_spec(target)
    assert _ordered(normalized) == _ordered(expected)
    assert stripped > 0
    assert len(_title_paths(normalize_spec.load_spec(source))) - len(_title_paths(normalized)) == stripped
    # What is left is the document title, docs metadata and example payloads.
    assert normalized["info"]["title"] == "Loops OpenAPI Spec"
    for path in _title_paths(normalized):
        assert path == ("info",) or any(part.startswith("x-") or part in ("example", "examples") for part in path), path
