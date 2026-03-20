"""Tests for pyloops.testing utilities."""

import json

import pytest
from httpx import Response

import pyloops
import pyloops.client
from pyloops.exceptions import LoopsError, LoopsRateLimitError
from pyloops.testing import loops_respx_mock

# ---------------------------------------------------------------------------
# Default success responses
# ---------------------------------------------------------------------------


@pytest.mark.asyncio
async def test_health():
    with loops_respx_mock() as api:
        client = pyloops.get_client()
        result = await client.health()
        assert result is True
        assert api["health"].called


@pytest.mark.asyncio
async def test_send_transactional_email():
    with loops_respx_mock() as api:
        client = pyloops.get_client()
        result = await client.send_transactional_email(
            transactional_id="tpl_abc",
            email="user@test.com",
            data_variables={"name": "Jan"},
        )
        assert result.success is True

        # Inspect the recorded request
        request = api["transactional"].calls[0].request
        body = json.loads(request.content)
        assert body["transactionalId"] == "tpl_abc"
        assert body["email"] == "user@test.com"
        assert body["dataVariables"]["name"] == "Jan"
        assert "Authorization" in request.headers


@pytest.mark.asyncio
async def test_create_contact():
    with loops_respx_mock() as api:
        client = pyloops.get_client()
        result = await client.create_contact(email="new@test.com", first_name="Ada")
        assert result.success is True
        assert api["create_contact"].called


@pytest.mark.asyncio
async def test_upsert_contact():
    with loops_respx_mock() as api:
        client = pyloops.get_client()
        result = await client.upsert_contact(email="user@test.com", first_name="Updated")
        assert result.success is True
        assert api["upsert_contact"].called


@pytest.mark.asyncio
async def test_find_contact():
    with loops_respx_mock() as api:
        client = pyloops.get_client()
        result = await client.find_contact(email="user@test.com")
        assert result is not None
        assert len(result) == 1
        assert api["find_contact"].called


@pytest.mark.asyncio
async def test_delete_contact():
    with loops_respx_mock() as api:
        client = pyloops.get_client()
        # delete_contact returns bool — the call should not raise
        _result = await client.delete_contact(email="user@test.com")
        assert api["delete_contact"].called


@pytest.mark.asyncio
async def test_send_event():
    with loops_respx_mock() as api:
        client = pyloops.get_client()
        result = await client.send_event(event_name="signup", email="user@test.com")
        assert result.success is True
        assert api["send_event"].called


@pytest.mark.asyncio
async def test_list_contact_properties():
    with loops_respx_mock() as api:
        client = pyloops.get_client()
        result = await client.list_contact_properties()
        assert result == []
        assert api["list_contact_properties"].called


@pytest.mark.asyncio
async def test_list_mailing_lists():
    with loops_respx_mock() as api:
        client = pyloops.get_client()
        result = await client.list_mailing_lists()
        assert result == []
        assert api["list_mailing_lists"].called


# ---------------------------------------------------------------------------
# Named route access
# ---------------------------------------------------------------------------


EXPECTED_ROUTE_NAMES = [
    "health",
    "transactional",
    "list_transactional",
    "create_contact",
    "upsert_contact",
    "find_contact",
    "delete_contact",
    "list_contact_properties",
    "create_contact_property",
    "send_event",
    "list_mailing_lists",
    "list_sending_ips",
]


def test_named_routes_accessible():
    with loops_respx_mock() as api:
        for name in EXPECTED_ROUTE_NAMES:
            route = api[name]
            assert route is not None, f"Route {name!r} not found"


# ---------------------------------------------------------------------------
# Request body inspection
# ---------------------------------------------------------------------------


@pytest.mark.asyncio
async def test_request_body_inspectable():
    with loops_respx_mock() as api:
        client = pyloops.get_client()
        await client.upsert_contact(email="inspect@test.com", first_name="Check")

        request = api["upsert_contact"].calls[0].request
        body = json.loads(request.content)
        assert body["email"] == "inspect@test.com"
        assert body["firstName"] == "Check"


# ---------------------------------------------------------------------------
# Custom route overrides (error simulation)
# ---------------------------------------------------------------------------


@pytest.mark.asyncio
async def test_override_429_rate_limit():
    with loops_respx_mock() as api:
        api["transactional"].mock(
            return_value=Response(
                429,
                json={"success": False, "message": "Rate limit exceeded"},
                headers={"x-ratelimit-limit": "10", "x-ratelimit-remaining": "0"},
            )
        )
        client = pyloops.get_client()
        with pytest.raises(LoopsRateLimitError) as exc_info:
            await client.send_transactional_email(transactional_id="abc", email="user@test.com")
        assert exc_info.value.limit == 10
        assert exc_info.value.remaining == 0


@pytest.mark.asyncio
async def test_override_400_bad_request():
    with loops_respx_mock() as api:
        api["send_event"].mock(return_value=Response(400, json={"success": False, "message": "Invalid event"}))
        client = pyloops.get_client()
        with pytest.raises(LoopsError, match="Invalid event"):
            await client.send_event(event_name="bad", email="user@test.com")


@pytest.mark.asyncio
async def test_override_404_transactional_not_found():
    with loops_respx_mock() as api:
        api["transactional"].mock(
            return_value=Response(
                404,
                json={
                    "success": False,
                    "message": "Transactional email not found",
                    "error": {"statusCode": 404, "message": "Not found"},
                },
            )
        )
        client = pyloops.get_client()
        with pytest.raises(LoopsError, match="not found"):
            await client.send_transactional_email(transactional_id="missing", email="user@test.com")


# ---------------------------------------------------------------------------
# assert_all_mocked behaviour
# ---------------------------------------------------------------------------


@pytest.mark.asyncio
async def test_unmatched_request_raises():
    """Requests to unregistered Loops API paths should raise."""
    with loops_respx_mock() as _api:
        client = pyloops.get_client()
        httpx_client = client._client.get_async_httpx_client()
        with pytest.raises(AssertionError, match="RESPX"):
            # /unknown-endpoint is not mocked — assert_all_mocked should reject it
            await httpx_client.get("https://app.loops.so/api/v1/unknown-endpoint")


# ---------------------------------------------------------------------------
# reset_client
# ---------------------------------------------------------------------------


def test_reset_client_clears_singleton():
    pyloops.configure(api_key="test-key")
    first = pyloops.get_client()
    pyloops.reset_client()
    second = pyloops.get_client()
    assert first is not second


# ---------------------------------------------------------------------------
# loops_respx_mock lifecycle
# ---------------------------------------------------------------------------


@pytest.mark.asyncio
async def test_mock_configures_api_key():
    """loops_respx_mock() should configure pyloops automatically."""
    with loops_respx_mock(api_key="custom-test-key") as api:
        client = pyloops.get_client()
        await client.health()
        # Verify the custom key was used in the Authorization header
        request = api["health"].calls[0].request
        assert "custom-test-key" in request.headers["Authorization"]


def test_mock_resets_singleton_on_exit():
    """The singleton should be cleared after the context manager exits."""
    with loops_respx_mock():
        pyloops.get_client()

    # After exit, the cached singleton should have been reset
    assert pyloops.client._client is None
