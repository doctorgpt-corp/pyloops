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


@pytest.mark.asyncio
async def test_create_contact_property():
    with loops_respx_mock() as api:
        client = pyloops.get_client()
        result = await client.create_contact_property(name="custom_prop", property_type="string")
        assert result["success"] is True
        assert result["key"] == "custom_prop"
        assert result["type"] == "string"

        request = api["create_contact_property"].calls[0].request
        body = json.loads(request.content)
        assert body["name"] == "custom_prop"
        assert body["type"] == "string"


@pytest.mark.asyncio
async def test_list_transactional_emails():
    with loops_respx_mock() as api:
        client = pyloops.get_client()
        result = await client.list_transactional_emails()
        assert result.pagination.total_results == 0
        assert result.data == []
        assert api["list_transactional"].called


@pytest.mark.asyncio
async def test_list_sending_ips():
    with loops_respx_mock() as api:
        client = pyloops.get_client()
        result = await client.list_sending_ips()
        assert result == []
        assert api["list_sending_ips"].called


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
    # 1.8.0
    "list_campaigns",
    "get_campaign",
    "create_campaign",
    "update_campaign",
    "list_components",
    "get_component",
    "list_themes",
    "get_theme",
    "get_email_message",
    "update_email_message",
    "get_contact_suppression",
    "remove_contact_suppression",
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


# ---------------------------------------------------------------------------
# Campaigns (1.8.0)
# ---------------------------------------------------------------------------


@pytest.mark.asyncio
async def test_list_campaigns():
    with loops_respx_mock() as api:
        client = pyloops.get_client()
        result = await client.list_campaigns()
        assert result.success is True
        assert result.data == []
        assert api["list_campaigns"].called


@pytest.mark.asyncio
async def test_get_campaign():
    with loops_respx_mock() as api:
        client = pyloops.get_client()
        result = await client.get_campaign("mock-campaign-id")
        assert result.success is True
        assert result.campaign_id == "mock-campaign-id"
        assert api["get_campaign"].called


@pytest.mark.asyncio
async def test_create_campaign():
    with loops_respx_mock() as api:
        client = pyloops.get_client()
        result = await client.create_campaign(name="My Campaign")
        assert result.success is True
        assert result.campaign_id == "mock-campaign-id"
        assert result.email_message_id == "mock-email-message-id"

        request = api["create_campaign"].calls[0].request
        body = json.loads(request.content)
        assert body["name"] == "My Campaign"


@pytest.mark.asyncio
async def test_update_campaign():
    with loops_respx_mock() as api:
        client = pyloops.get_client()
        result = await client.update_campaign("mock-campaign-id", name="Updated Campaign")
        assert result.success is True
        assert result.name == "Updated Campaign"

        request = api["update_campaign"].calls[0].request
        body = json.loads(request.content)
        assert body["name"] == "Updated Campaign"


# ---------------------------------------------------------------------------
# Components (1.8.0)
# ---------------------------------------------------------------------------


@pytest.mark.asyncio
async def test_list_components():
    with loops_respx_mock() as api:
        client = pyloops.get_client()
        result = await client.list_components()
        assert result.success is True
        assert result.data == []
        assert api["list_components"].called


@pytest.mark.asyncio
async def test_get_component():
    with loops_respx_mock() as api:
        client = pyloops.get_client()
        result = await client.get_component("mock-component-id")
        assert result.success is True
        assert result.component_id == "mock-component-id"
        assert result.name == "Mock Component"
        assert api["get_component"].called


# ---------------------------------------------------------------------------
# Themes (1.8.0)
# ---------------------------------------------------------------------------


@pytest.mark.asyncio
async def test_list_themes():
    with loops_respx_mock() as api:
        client = pyloops.get_client()
        result = await client.list_themes()
        assert result.success is True
        assert result.data == []
        assert api["list_themes"].called


@pytest.mark.asyncio
async def test_get_theme():
    with loops_respx_mock() as api:
        client = pyloops.get_client()
        result = await client.get_theme("mock-theme-id")
        assert result.success is True
        assert result.theme_id == "mock-theme-id"
        assert result.name == "Mock Theme"
        assert api["get_theme"].called


# ---------------------------------------------------------------------------
# Email Messages (1.8.0)
# ---------------------------------------------------------------------------


@pytest.mark.asyncio
async def test_get_email_message():
    with loops_respx_mock() as api:
        client = pyloops.get_client()
        result = await client.get_email_message("mock-email-message-id")
        assert result.success is True
        assert result.email_message_id == "mock-email-message-id"
        assert result.subject == "Mock Subject"
        assert api["get_email_message"].called


@pytest.mark.asyncio
async def test_update_email_message():
    with loops_respx_mock() as api:
        client = pyloops.get_client()
        result = await client.update_email_message(
            "mock-email-message-id",
            subject="New Subject",
            from_name="Alice",
        )
        assert result.success is True

        request = api["update_email_message"].calls[0].request
        body = json.loads(request.content)
        assert body["subject"] == "New Subject"
        assert body["fromName"] == "Alice"
        assert "email" not in body  # unset fields should be omitted


# ---------------------------------------------------------------------------
# Contact Suppression (1.8.0)
# ---------------------------------------------------------------------------


@pytest.mark.asyncio
async def test_get_contact_suppression():
    with loops_respx_mock() as api:
        client = pyloops.get_client()
        result = await client.get_contact_suppression(email="user@test.com")
        assert result.is_suppressed is False
        assert result.removal_quota.remaining == 3
        assert api["get_contact_suppression"].called


@pytest.mark.asyncio
async def test_remove_contact_suppression():
    with loops_respx_mock() as api:
        client = pyloops.get_client()
        result = await client.remove_contact_suppression(email="user@test.com")
        assert result.success is True
        assert result.removal_quota.remaining == 2
        assert api["remove_contact_suppression"].called


@pytest.mark.asyncio
async def test_suppression_requires_email_or_user_id():
    with loops_respx_mock():
        client = pyloops.get_client()
        with pytest.raises(LoopsError, match="Either email or user_id must be provided"):
            await client.get_contact_suppression()
        with pytest.raises(LoopsError, match="Either email or user_id must be provided"):
            await client.remove_contact_suppression()


# ---------------------------------------------------------------------------
# Error simulation — 1.8.0 methods
# ---------------------------------------------------------------------------

_FAILURE_JSON = {"success": False, "message": "Something went wrong"}


@pytest.mark.asyncio
async def test_list_campaigns_400():
    with loops_respx_mock() as api:
        api["list_campaigns"].mock(return_value=Response(400, json=_FAILURE_JSON))
        client = pyloops.get_client()
        with pytest.raises(LoopsError, match="Something went wrong"):
            await client.list_campaigns()


@pytest.mark.asyncio
async def test_get_campaign_404():
    with loops_respx_mock() as api:
        api["get_campaign"].mock(return_value=Response(404, json=_FAILURE_JSON))
        client = pyloops.get_client()
        with pytest.raises(LoopsError, match="Something went wrong"):
            await client.get_campaign("missing-id")


@pytest.mark.asyncio
async def test_create_campaign_400():
    with loops_respx_mock() as api:
        api["create_campaign"].mock(return_value=Response(400, json=_FAILURE_JSON))
        client = pyloops.get_client()
        with pytest.raises(LoopsError, match="Something went wrong"):
            await client.create_campaign(name="Bad Campaign")


@pytest.mark.asyncio
async def test_update_campaign_404():
    with loops_respx_mock() as api:
        api["update_campaign"].mock(return_value=Response(404, json=_FAILURE_JSON))
        client = pyloops.get_client()
        with pytest.raises(LoopsError, match="Something went wrong"):
            await client.update_campaign("missing-id", name="x")


@pytest.mark.asyncio
async def test_list_components_400():
    with loops_respx_mock() as api:
        api["list_components"].mock(return_value=Response(400, json=_FAILURE_JSON))
        client = pyloops.get_client()
        with pytest.raises(LoopsError, match="Something went wrong"):
            await client.list_components()


@pytest.mark.asyncio
async def test_get_component_404():
    with loops_respx_mock() as api:
        api["get_component"].mock(return_value=Response(404, json=_FAILURE_JSON))
        client = pyloops.get_client()
        with pytest.raises(LoopsError, match="Something went wrong"):
            await client.get_component("missing-id")


@pytest.mark.asyncio
async def test_list_themes_400():
    with loops_respx_mock() as api:
        api["list_themes"].mock(return_value=Response(400, json=_FAILURE_JSON))
        client = pyloops.get_client()
        with pytest.raises(LoopsError, match="Something went wrong"):
            await client.list_themes()


@pytest.mark.asyncio
async def test_get_theme_404():
    with loops_respx_mock() as api:
        api["get_theme"].mock(return_value=Response(404, json=_FAILURE_JSON))
        client = pyloops.get_client()
        with pytest.raises(LoopsError, match="Something went wrong"):
            await client.get_theme("missing-id")


@pytest.mark.asyncio
async def test_get_email_message_404():
    with loops_respx_mock() as api:
        api["get_email_message"].mock(return_value=Response(404, json=_FAILURE_JSON))
        client = pyloops.get_client()
        with pytest.raises(LoopsError, match="Something went wrong"):
            await client.get_email_message("missing-id")


@pytest.mark.asyncio
async def test_update_email_message_400():
    with loops_respx_mock() as api:
        api["update_email_message"].mock(return_value=Response(400, json=_FAILURE_JSON))
        client = pyloops.get_client()
        with pytest.raises(LoopsError, match="Something went wrong"):
            await client.update_email_message("msg-id", subject="x")


@pytest.mark.asyncio
async def test_get_contact_suppression_400():
    with loops_respx_mock() as api:
        api["get_contact_suppression"].mock(return_value=Response(400, json=_FAILURE_JSON))
        client = pyloops.get_client()
        with pytest.raises(LoopsError, match="Something went wrong"):
            await client.get_contact_suppression(email="user@test.com")


@pytest.mark.asyncio
async def test_remove_contact_suppression_400():
    with loops_respx_mock() as api:
        api["remove_contact_suppression"].mock(return_value=Response(400, json=_FAILURE_JSON))
        client = pyloops.get_client()
        with pytest.raises(LoopsError, match="Something went wrong"):
            await client.remove_contact_suppression(email="user@test.com")


@pytest.mark.asyncio
async def test_campaigns_rate_limit():
    with loops_respx_mock() as api:
        api["list_campaigns"].mock(
            return_value=Response(
                429,
                json={"success": False},
                headers={"x-ratelimit-limit": "5", "x-ratelimit-remaining": "0"},
            )
        )
        client = pyloops.get_client()
        with pytest.raises(LoopsRateLimitError) as exc_info:
            await client.list_campaigns()
        assert exc_info.value.limit == 5
        assert exc_info.value.remaining == 0
