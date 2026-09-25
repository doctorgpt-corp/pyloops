import atexit
from contextlib import ExitStack
from functools import cache
from importlib.resources import as_file, files
from pathlib import Path

_materialised = ExitStack()
atexit.register(_materialised.close)


@cache
def openapi_spec_path() -> Path:
    """Filesystem path of the Loops OpenAPI spec this client was generated from."""
    return _materialised.enter_context(as_file(files("pyloops") / "openapi.yaml"))
