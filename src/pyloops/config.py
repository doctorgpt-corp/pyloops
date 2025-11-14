import os

_default_api_key: str | None = None
_default_base_url: str = "https://app.loops.so/api/v1"


def configure(api_key: str | None = None, base_url: str | None = None) -> None:
    """
    Configure default settings for pyloops.

    Args:
        api_key: Loops API key. If not provided, will fall back to LOOPS_API_KEY env var.
        base_url: Base URL for Loops API (default: https://app.loops.so/api/v1)
    """
    global _default_api_key, _default_base_url
    if api_key is not None:
        _default_api_key = api_key
    if base_url is not None:
        _default_base_url = base_url


def get_config() -> dict[str, str | None]:
    api_key = _default_api_key or os.getenv("LOOPS_API_KEY")
    return {"api_key": api_key, "base_url": _default_base_url}
