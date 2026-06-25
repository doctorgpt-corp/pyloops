"""Tests for base_url normalization.

As of the Loops API v1.14.x update, the ``/v1`` version segment moved from the
base URL into each endpoint path. pyloops strips a trailing ``/v1`` from the
configured base URL (emitting a ``DeprecationWarning``) so that consumers who
pinned the old default ``https://app.loops.so/api/v1`` keep working.
"""

import warnings

import pytest

from pyloops.client import LoopsClient


@pytest.mark.parametrize(
    ("given", "expected"),
    [
        ("https://app.loops.so/api", "https://app.loops.so/api"),
        ("https://app.loops.so/api/", "https://app.loops.so/api"),
        ("https://app.loops.so/api/v1", "https://app.loops.so/api"),
        ("https://app.loops.so/api/v1/", "https://app.loops.so/api"),
        ("https://proxy.internal/loops/v1", "https://proxy.internal/loops"),
    ],
)
def test_normalize_base_url(given, expected):
    with warnings.catch_warnings():
        warnings.simplefilter("ignore", DeprecationWarning)
        assert LoopsClient._normalize_base_url(given) == expected


def test_trailing_v1_emits_deprecation_warning():
    with pytest.warns(DeprecationWarning, match="/v1"):
        LoopsClient._normalize_base_url("https://app.loops.so/api/v1")


def test_clean_base_url_does_not_warn():
    with warnings.catch_warnings():
        warnings.simplefilter("error")  # any warning becomes an error
        assert LoopsClient._normalize_base_url("https://app.loops.so/api") == "https://app.loops.so/api"


def test_client_constructor_strips_v1_and_warns():
    with pytest.warns(DeprecationWarning, match="/v1"):
        client = LoopsClient(api_key="test-key", base_url="https://app.loops.so/api/v1")
    httpx_base = str(client._client.get_async_httpx_client().base_url)
    assert "/v1" not in httpx_base
    assert httpx_base.rstrip("/") == "https://app.loops.so/api"
