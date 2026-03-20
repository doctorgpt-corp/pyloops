import os
from typing import TypedDict


class LoopsConfig(TypedDict):
    api_key: str | None
    base_url: str
    safe_mode: bool
    safe_mode_allowed_domains: tuple[str, ...]


_default_api_key: str | None = None
_default_base_url: str = "https://app.loops.so/api/v1"
_default_safe_mode: bool = False
_default_safe_mode_allowed_domains: tuple[str, ...] = ()


def configure(
    api_key: str | None = None,
    base_url: str | None = None,
    safe_mode: bool | None = None,
    safe_mode_allowed_domains: tuple[str, ...] | None = None,
) -> None:
    """
    Configure default settings for pyloops.

    Args:
        api_key: Loops API key. If not provided, will fall back to LOOPS_API_KEY env var.
        base_url: Base URL for Loops API (default: https://app.loops.so/api/v1)
        safe_mode: If True, only allow emails to domains in safe_mode_allowed_domains.
            Useful for local development to prevent accidentally emailing real users.
        safe_mode_allowed_domains: Tuple of allowed email domains when safe_mode is enabled
            (e.g. ("@test.com", "@example.com")). Each entry should start with "@".
    """
    global _default_api_key, _default_base_url, _default_safe_mode, _default_safe_mode_allowed_domains
    if api_key is not None:
        _default_api_key = api_key
    if base_url is not None:
        _default_base_url = base_url
    if safe_mode is not None:
        _default_safe_mode = safe_mode
    if safe_mode_allowed_domains is not None:
        _default_safe_mode_allowed_domains = safe_mode_allowed_domains


def get_config() -> LoopsConfig:
    api_key = _default_api_key or os.getenv("LOOPS_API_KEY")
    return {
        "api_key": api_key,
        "base_url": _default_base_url,
        "safe_mode": _default_safe_mode,
        "safe_mode_allowed_domains": _default_safe_mode_allowed_domains,
    }
