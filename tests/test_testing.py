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
    # 1.14.x
    "list_transactional_templates",
    "get_transactional_template",
    "create_transactional_template",
    "update_transactional_template",
    "draft_transactional_template",
    "publish_transactional_template",
    "create_upload",
    "complete_upload",
    "list_workflows",
    "get_workflow",
    "get_workflow_node",
    "list_audience_segments",
    "get_audience_segment",
    "list_campaign_groups",
    "get_campaign_group",
    "create_campaign_group",
    "update_campaign_group",
    "list_transactional_groups",
    "get_transactional_group",
    "create_transactional_group",
    "update_transactional_group",
    "preview_email_message",
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
        assert result.data == []
        assert api["list_campaigns"].called


@pytest.mark.asyncio
async def test_get_campaign():
    with loops_respx_mock() as api:
        client = pyloops.get_client()
        result = await client.get_campaign("mock-campaign-id")
        assert result.id == "mock-campaign-id"
        assert api["get_campaign"].called


@pytest.mark.asyncio
async def test_create_campaign():
    with loops_respx_mock() as api:
        client = pyloops.get_client()
        result = await client.create_campaign(name="My Campaign")
        assert result.id == "mock-campaign-id"
        assert result.email_message_id == "mock-email-message-id"

        request = api["create_campaign"].calls[0].request
        body = json.loads(request.content)
        assert body["name"] == "My Campaign"


@pytest.mark.asyncio
async def test_update_campaign():
    with loops_respx_mock() as api:
        client = pyloops.get_client()
        result = await client.update_campaign("mock-campaign-id", name="Updated Campaign")
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
        assert result.data == []
        assert api["list_components"].called


@pytest.mark.asyncio
async def test_get_component():
    with loops_respx_mock() as api:
        client = pyloops.get_client()
        result = await client.get_component("mock-component-id")
        assert result.id == "mock-component-id"
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
        assert result.data == []
        assert api["list_themes"].called


@pytest.mark.asyncio
async def test_get_theme():
    with loops_respx_mock() as api:
        client = pyloops.get_client()
        result = await client.get_theme("mock-theme-id")
        assert result.id == "mock-theme-id"
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
        assert result.id == "mock-email-message-id"
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
        assert result.id == "mock-email-message-id"

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


# ---------------------------------------------------------------------------
# New endpoint families (1.14.x)
# ---------------------------------------------------------------------------


@pytest.mark.asyncio
async def test_list_transactional_templates():
    with loops_respx_mock() as api:
        client = pyloops.get_client()
        result = await client.list_transactional_templates()
        assert result.data == []
        assert api["list_transactional_templates"].called


@pytest.mark.asyncio
async def test_get_transactional_template():
    with loops_respx_mock() as api:
        client = pyloops.get_client()
        result = await client.get_transactional_template("mock-transactional-id")
        assert result.id == "mock-transactional-id"
        assert api["get_transactional_template"].called


@pytest.mark.asyncio
async def test_create_transactional_template():
    with loops_respx_mock() as api:
        client = pyloops.get_client()
        result = await client.create_transactional_template(name="My Template", transactional_group_id="grp-1")
        assert result.id == "mock-transactional-id"
        body = json.loads(api["create_transactional_template"].calls[0].request.content)
        assert body["name"] == "My Template"
        assert body["transactionalGroupId"] == "grp-1"


@pytest.mark.asyncio
async def test_update_transactional_template():
    with loops_respx_mock() as api:
        client = pyloops.get_client()
        result = await client.update_transactional_template("mock-transactional-id", name="Renamed")
        assert result.id == "mock-transactional-id"
        body = json.loads(api["update_transactional_template"].calls[0].request.content)
        assert body["name"] == "Renamed"
        assert "transactionalGroupId" not in body  # UNSET omitted


@pytest.mark.asyncio
async def test_draft_transactional_template():
    with loops_respx_mock() as api:
        client = pyloops.get_client()
        result = await client.draft_transactional_template("mock-transactional-id")
        assert result.id == "mock-transactional-id"
        assert api["draft_transactional_template"].called


@pytest.mark.asyncio
async def test_publish_transactional_template():
    with loops_respx_mock() as api:
        client = pyloops.get_client()
        result = await client.publish_transactional_template("mock-transactional-id")
        assert result.id == "mock-transactional-id"
        assert api["publish_transactional_template"].called


@pytest.mark.asyncio
async def test_create_upload():
    with loops_respx_mock() as api:
        client = pyloops.get_client()
        result = await client.create_upload(content_type="image/png", content_length=1234)
        assert result.email_asset_id == "mock-asset-id"
        body = json.loads(api["create_upload"].calls[0].request.content)
        assert body["contentType"] == "image/png"
        assert body["contentLength"] == 1234


@pytest.mark.asyncio
async def test_complete_upload():
    with loops_respx_mock() as api:
        client = pyloops.get_client()
        result = await client.complete_upload("mock-asset-id")
        assert result.final_url == "https://example.com/final.png"
        assert api["complete_upload"].called


@pytest.mark.asyncio
async def test_complete_upload_limit_exceeded():
    # The upload-limit-exceeded response uses HTTP 429, which pyloops surfaces
    # uniformly as a rate-limit error.
    with loops_respx_mock() as api:
        api["complete_upload"].mock(
            return_value=Response(
                429,
                json={"message": "Upload limit exceeded"},
                headers={"x-ratelimit-limit": "100", "x-ratelimit-remaining": "0"},
            )
        )
        client = pyloops.get_client()
        with pytest.raises(LoopsRateLimitError) as exc_info:
            await client.complete_upload("mock-asset-id")
        assert exc_info.value.limit == 100
        assert exc_info.value.remaining == 0


@pytest.mark.asyncio
async def test_complete_upload_error():
    with loops_respx_mock() as api:
        api["complete_upload"].mock(return_value=Response(400, json={"message": "Bad upload"}))
        client = pyloops.get_client()
        with pytest.raises(LoopsError, match="Bad upload"):
            await client.complete_upload("mock-asset-id")


@pytest.mark.asyncio
async def test_list_workflows():
    with loops_respx_mock() as api:
        client = pyloops.get_client()
        result = await client.list_workflows()
        assert result.data == []
        assert api["list_workflows"].called


@pytest.mark.asyncio
async def test_get_workflow():
    with loops_respx_mock() as api:
        client = pyloops.get_client()
        result = await client.get_workflow("mock-workflow-id")
        assert result.id == "mock-workflow-id"
        assert api["get_workflow"].called


@pytest.mark.asyncio
async def test_get_workflow_node():
    with loops_respx_mock() as api:
        client = pyloops.get_client()
        result = await client.get_workflow_node("mock-workflow-id", "mock-node-id")
        assert result.id == "mock-node-id"
        assert api["get_workflow_node"].called


@pytest.mark.asyncio
async def test_list_audience_segments():
    with loops_respx_mock() as api:
        client = pyloops.get_client()
        result = await client.list_audience_segments()
        assert result.data == []
        assert api["list_audience_segments"].called


@pytest.mark.asyncio
async def test_get_audience_segment():
    with loops_respx_mock() as api:
        client = pyloops.get_client()
        result = await client.get_audience_segment("mock-segment-id")
        assert result.id == "mock-segment-id"
        assert api["get_audience_segment"].called


@pytest.mark.asyncio
async def test_list_campaign_groups():
    with loops_respx_mock() as api:
        client = pyloops.get_client()
        result = await client.list_campaign_groups()
        assert result.data == []
        assert api["list_campaign_groups"].called


@pytest.mark.asyncio
async def test_get_campaign_group():
    with loops_respx_mock() as api:
        client = pyloops.get_client()
        result = await client.get_campaign_group("mock-group-id")
        assert result.id == "mock-group-id"
        assert api["get_campaign_group"].called


@pytest.mark.asyncio
async def test_create_campaign_group():
    with loops_respx_mock() as api:
        client = pyloops.get_client()
        result = await client.create_campaign_group(name="Group A", description="desc")
        assert result.id == "mock-group-id"
        body = json.loads(api["create_campaign_group"].calls[0].request.content)
        assert body["name"] == "Group A"
        assert body["description"] == "desc"


@pytest.mark.asyncio
async def test_update_campaign_group():
    with loops_respx_mock() as api:
        client = pyloops.get_client()
        result = await client.update_campaign_group("mock-group-id", name="Group B")
        assert result.id == "mock-group-id"
        body = json.loads(api["update_campaign_group"].calls[0].request.content)
        assert body["name"] == "Group B"


@pytest.mark.asyncio
async def test_list_transactional_groups():
    with loops_respx_mock() as api:
        client = pyloops.get_client()
        result = await client.list_transactional_groups()
        assert result.data == []
        assert api["list_transactional_groups"].called


@pytest.mark.asyncio
async def test_get_transactional_group():
    with loops_respx_mock() as api:
        client = pyloops.get_client()
        result = await client.get_transactional_group("mock-group-id")
        assert result.id == "mock-group-id"
        assert api["get_transactional_group"].called


@pytest.mark.asyncio
async def test_create_transactional_group():
    with loops_respx_mock() as api:
        client = pyloops.get_client()
        result = await client.create_transactional_group(name="TGroup")
        assert result.id == "mock-group-id"
        assert api["create_transactional_group"].called


@pytest.mark.asyncio
async def test_update_transactional_group():
    with loops_respx_mock() as api:
        client = pyloops.get_client()
        result = await client.update_transactional_group("mock-group-id", description="new desc")
        assert result.id == "mock-group-id"
        body = json.loads(api["update_transactional_group"].calls[0].request.content)
        assert body["description"] == "new desc"


@pytest.mark.asyncio
async def test_preview_email_message():
    with loops_respx_mock() as api:
        client = pyloops.get_client()
        result = await client.preview_email_message(
            "mock-email-message-id",
            emails=["user@test.com"],
            data_variables={"name": "Jan"},
        )
        assert result.id == "mock-preview-id"
        body = json.loads(api["preview_email_message"].calls[0].request.content)
        assert body["emails"] == ["user@test.com"]
        assert body["dataVariables"] == {"name": "Jan"}


@pytest.mark.asyncio
async def test_get_workflow_not_found():
    with loops_respx_mock() as api:
        api["get_workflow"].mock(return_value=Response(404, json={"message": "Workflow not found"}))
        client = pyloops.get_client()
        with pytest.raises(LoopsError, match="Workflow not found"):
            await client.get_workflow("missing")


@pytest.mark.asyncio
async def test_create_campaign_group_error():
    with loops_respx_mock() as api:
        api["create_campaign_group"].mock(return_value=Response(400, json={"message": "Invalid group"}))
        client = pyloops.get_client()
        with pytest.raises(LoopsError, match="Invalid group"):
            await client.create_campaign_group(name="bad")


@pytest.mark.asyncio
async def test_list_workflows_rate_limit():
    with loops_respx_mock() as api:
        api["list_workflows"].mock(
            return_value=Response(
                429,
                json={"success": False},
                headers={"x-ratelimit-limit": "7", "x-ratelimit-remaining": "0"},
            )
        )
        client = pyloops.get_client()
        with pytest.raises(LoopsRateLimitError) as exc_info:
            await client.list_workflows()
        assert exc_info.value.limit == 7
        assert exc_info.value.remaining == 0


# ---------------------------------------------------------------------------
# Error-path coverage for the new 1.14.x wrappers
# ---------------------------------------------------------------------------

# (route_name, call) for every new wrapper not already given a standalone error
# test above (complete_upload, get_workflow, create_campaign_group are covered
# separately). A 400 on the mocked route must surface as a LoopsError.
_NEW_WRAPPER_ERROR_CASES = [
    ("list_transactional_templates", lambda c: c.list_transactional_templates()),
    ("get_transactional_template", lambda c: c.get_transactional_template("x")),
    ("create_transactional_template", lambda c: c.create_transactional_template(name="x")),
    ("update_transactional_template", lambda c: c.update_transactional_template("x", name="y")),
    ("draft_transactional_template", lambda c: c.draft_transactional_template("x")),
    ("publish_transactional_template", lambda c: c.publish_transactional_template("x")),
    ("create_upload", lambda c: c.create_upload(content_type="image/png", content_length=1)),
    ("get_workflow_node", lambda c: c.get_workflow_node("wf", "node")),
    ("list_workflows", lambda c: c.list_workflows()),
    ("list_audience_segments", lambda c: c.list_audience_segments()),
    ("get_audience_segment", lambda c: c.get_audience_segment("x")),
    ("list_campaign_groups", lambda c: c.list_campaign_groups()),
    ("get_campaign_group", lambda c: c.get_campaign_group("x")),
    ("update_campaign_group", lambda c: c.update_campaign_group("x", name="y")),
    ("list_transactional_groups", lambda c: c.list_transactional_groups()),
    ("get_transactional_group", lambda c: c.get_transactional_group("x")),
    ("create_transactional_group", lambda c: c.create_transactional_group(name="x")),
    ("update_transactional_group", lambda c: c.update_transactional_group("x", name="y")),
    ("preview_email_message", lambda c: c.preview_email_message("x", emails=["user@test.com"])),
]


@pytest.mark.parametrize(
    ("route_name", "call"),
    _NEW_WRAPPER_ERROR_CASES,
    ids=[name for name, _ in _NEW_WRAPPER_ERROR_CASES],
)
@pytest.mark.asyncio
async def test_new_wrapper_error_path(route_name, call):
    with loops_respx_mock() as api:
        api[route_name].mock(return_value=Response(400, json={"message": "boom"}))
        client = pyloops.get_client()
        with pytest.raises(LoopsError):
            await call(client)


# ---------------------------------------------------------------------------
# Legacy base_url override still matches mock routes (regression)
# ---------------------------------------------------------------------------


@pytest.mark.asyncio
async def test_legacy_v1_base_url_still_matches_routes():
    # A caller pinned to the old ".../api/v1" default: LoopsClient strips the
    # trailing /v1 and loops_respx_mock() must normalize the router to match.
    import warnings

    with warnings.catch_warnings():
        warnings.simplefilter("ignore", DeprecationWarning)
        with loops_respx_mock(base_url="https://app.loops.so/api/v1") as api:
            client = pyloops.get_client()
            assert await client.health() is True
            assert api["health"].called
