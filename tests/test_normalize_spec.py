import importlib.util
import json
from pathlib import Path

import pyloops

SCRIPT = Path(__file__).parent.parent / "scripts" / "normalize_spec.py"

_spec = importlib.util.spec_from_file_location("normalize_spec", SCRIPT)
assert _spec and _spec.loader
normalize_spec = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(normalize_spec)


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
    assert "title" not in json.dumps(spec)


def test_strips_titles_from_schemas_inlined_in_paths():
    spec = {
        "paths": {
            "/v1/things": {
                "post": {
                    "parameters": [{"name": "q", "in": "query", "schema": {"title": "Query", "type": "string"}}],
                    "requestBody": {
                        "content": {"application/json": {"schema": {"title": "Body", "type": "object"}}},
                    },
                    "responses": {
                        "200": {"content": {"application/json": {"schema": {"title": "Result", "type": "object"}}}}
                    },
                }
            }
        }
    }

    assert normalize_spec.normalize(spec) == 3
    assert "title" not in json.dumps(spec)


def test_keeps_titles_that_do_not_name_a_schema():
    spec = {
        "info": {"title": "Loops OpenAPI Spec"},
        "paths": {"/v1/things": {"get": {"x-mint": {"metadata": {"title": "List things"}}}}},
        "components": {
            "schemas": {
                "Rule": {
                    "type": "object",
                    "properties": {"title": {"type": "string"}},
                    "required": ["title"],
                    "example": {"title": "Missing button link"},
                    "examples": [{"title": "Missing text link"}],
                    "default": {"title": "Untitled"},
                }
            }
        },
    }
    untouched = json.loads(json.dumps(spec))

    assert normalize_spec.normalize(spec) == 0
    assert spec == untouched


def test_keeps_timestamps_as_strings(tmp_path):
    source = tmp_path / "spec.yaml"
    source.write_text("components:\n  schemas:\n    Thing:\n      examples:\n        - 2026-01-02T03:04:05Z\n")

    spec = normalize_spec.load_spec(source)

    assert spec["components"]["schemas"]["Thing"]["examples"] == ["2026-01-02T03:04:05Z"]


def test_shipped_spec_normalizes_to_unique_schema_names(tmp_path):
    target = tmp_path / "normalized.json"

    assert normalize_spec.main(["normalize_spec", str(pyloops.openapi_spec_path()), str(target)]) == 0

    normalized = json.loads(target.read_text())
    assert normalized["info"]["title"] == "Loops OpenAPI Spec"
    assert not [name for name, schema in normalized["components"]["schemas"].items() if "title" in schema]
