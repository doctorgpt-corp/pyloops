import re
from pathlib import Path

import yaml

import pyloops

GENERATED_API = Path(pyloops.__file__).parent / "_generated" / "api"
HTTP_METHODS = {"get", "put", "post", "delete", "patch", "head", "options", "trace"}


def _normalise(path: str) -> str:
    return re.sub(r"\{[^}]*\}", "{}", path)


def _client_operations() -> set[tuple[str, str]]:
    operations = set()
    for module in GENERATED_API.glob("*/*.py"):
        source = module.read_text()
        method = re.search(r'"method": "(\w+)"', source)
        url = re.search(r'"url": f?"([^"]+)"', source)
        if method and url:
            operations.add((method.group(1), _normalise(url.group(1))))
    return operations


def _spec() -> dict:
    return yaml.safe_load(pyloops.openapi_spec_path().read_text())


def test_spec_path_is_a_file():
    path = pyloops.openapi_spec_path()

    assert path.is_file()


def test_spec_is_an_openapi_document():
    spec = _spec()

    assert spec["openapi"].startswith("3.")
    assert spec["paths"]


def test_spec_lists_every_operation_the_client_calls():
    spec_operations = {
        (method, _normalise(path))
        for path, item in _spec()["paths"].items()
        for method in item
        if method in HTTP_METHODS
    }

    client_operations = _client_operations()

    assert len(client_operations) == len(list(GENERATED_API.glob("*/[!_]*.py")))
    assert client_operations <= spec_operations
