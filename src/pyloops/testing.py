"""
Testing utilities for pyloops consumers.

Provides a respx-based mock that intercepts all Loops API HTTP calls at the
transport level, so the real pyloops client code runs end-to-end but no actual
API requests leave the process.

Requires the ``[testing]`` extra::

    pip install pyloops[testing]

Quick-start::

    import json

    import pyloops
    from pyloops.testing import loops_respx_mock

    with loops_respx_mock() as loops_api:
        client = pyloops.get_client()
        await client.send_transactional_email(
            transactional_id="abc",
            email="user@test.com",
            data_variables={"name": "Jan"},
        )

        # Inspect the HTTP request that pyloops made
        request = loops_api["transactional"].calls[0].request
        body = json.loads(request.content)
        assert body["transactionalId"] == "abc"

Error simulation::

    from httpx import Response
    from pyloops.testing import loops_respx_mock

    with loops_respx_mock() as loops_api:
        loops_api["transactional"].mock(return_value=Response(429, json={"success": False}))
        # client.send_transactional_email(...) will now raise LoopsRateLimitError

Recommended pytest fixture::

    import pytest
    from pyloops.testing import loops_respx_mock

    @pytest.fixture
    def loops_api():
        with loops_respx_mock() as router:
            yield router
"""

from collections.abc import Iterator
from contextlib import contextmanager

import pyloops

try:
    import respx
except ImportError as exc:
    raise ImportError(
        "respx is required for pyloops testing utilities. Install it with: pip install pyloops[testing]"
    ) from exc

BASE_URL = "https://app.loops.so/api"


@contextmanager
def loops_respx_mock(
    *,
    api_key: str = "test-key",
    base_url: str = BASE_URL,
    assert_all_mocked: bool = True,
    safe_mode: bool = False,
    safe_mode_allowed_domains: tuple[str, ...] = (),
) -> Iterator[respx.Router]:
    """Return a context manager that mocks every Loops API endpoint.

    On enter, configures pyloops with the given *api_key* and resets the
    singleton client so a fresh instance is created against the mock. On exit
    the singleton is reset again to prevent test state from leaking.

    All routes return a successful response by default and are accessible by
    name on the yielded router (e.g. ``router["transactional"]``).

    Args:
        api_key: API key to configure pyloops with (default: ``"test-key"``).
        base_url: The Loops API base URL to intercept. Override this only if
            you configured ``pyloops`` with a custom ``base_url``.
        assert_all_mocked: When *True* (the default), any httpx request that
            does not match a mocked route will raise immediately, preventing
            accidental real API calls.
        safe_mode: When *True*, the client will only allow emails to domains
            in *safe_mode_allowed_domains*. Defaults to *False* so tests can
            use any email address.
        safe_mode_allowed_domains: Tuple of allowed email domains when
            *safe_mode* is enabled (e.g. ``("@test.com",)``).
    """
    pyloops.configure(
        api_key=api_key,
        base_url=base_url,
        safe_mode=safe_mode,
        safe_mode_allowed_domains=safe_mode_allowed_domains,
    )
    pyloops.reset_client()
    # LoopsClient strips a trailing "/v1" from base_url (see
    # LoopsClient._normalize_base_url), so the router must listen on the same
    # normalized URL — otherwise a legacy ".../api/v1" override would make the
    # client request "/api/v1/..." while respx listens under "/api/v1/v1/...".
    normalized_base_url = base_url.rstrip("/")
    if normalized_base_url.endswith("/v1"):
        normalized_base_url = normalized_base_url[: -len("/v1")]
    with respx.mock(
        base_url=normalized_base_url, assert_all_called=False, assert_all_mocked=assert_all_mocked
    ) as router:
        # Health / API key validation
        router.get("/v1/api-key", name="health").mock(
            return_value=respx.MockResponse(200, json={"success": True, "teamName": "Test"})
        )

        # Transactional emails
        router.post("/v1/transactional", name="transactional").mock(
            return_value=respx.MockResponse(200, json={"success": True})
        )
        router.get("/v1/transactional", name="list_transactional").mock(
            return_value=respx.MockResponse(
                200,
                json={
                    "pagination": {
                        "totalResults": 0,
                        "returnedResults": 0,
                        "perPage": 20,
                        "totalPages": 0,
                    },
                    "data": [],
                },
            )
        )

        # Contacts
        router.post("/v1/contacts/create", name="create_contact").mock(
            return_value=respx.MockResponse(200, json={"success": True, "id": "mock-contact-id"})
        )
        router.put("/v1/contacts/update", name="upsert_contact").mock(
            return_value=respx.MockResponse(200, json={"success": True, "id": "mock-contact-id"})
        )
        router.get("/v1/contacts/find", name="find_contact").mock(
            return_value=respx.MockResponse(
                200,
                json=[
                    {
                        "id": "mock-contact-id",
                        "email": "user@test.com",
                        "firstName": "Test",
                        "lastName": "User",
                    }
                ],
            )
        )
        router.post("/v1/contacts/delete", name="delete_contact").mock(
            return_value=respx.MockResponse(200, json={"message": "Contact deleted.", "success": True})
        )

        # Contact properties
        router.get("/v1/contacts/properties", name="list_contact_properties").mock(
            return_value=respx.MockResponse(200, json=[])
        )
        router.post("/v1/contacts/properties", name="create_contact_property").mock(
            return_value=respx.MockResponse(
                200, json={"success": True, "key": "custom_prop", "label": "Custom Prop", "type": "string"}
            )
        )

        # Events
        router.post("/v1/events/send", name="send_event").mock(
            return_value=respx.MockResponse(200, json={"success": True})
        )

        # Mailing lists
        router.get("/v1/lists", name="list_mailing_lists").mock(return_value=respx.MockResponse(200, json=[]))

        # Dedicated sending IPs
        router.get("/v1/dedicated-sending-ips", name="list_sending_ips").mock(
            return_value=respx.MockResponse(200, json=[])
        )

        # Campaigns
        _pagination = {"totalResults": 0, "returnedResults": 0, "perPage": 20, "totalPages": 0, "nextCursor": None}
        # Fields added to campaign responses in the Loops API v1.14.x update.
        _campaign_targeting = {
            "campaignGroupId": None,
            "mailingListId": None,
            "audienceSegmentId": None,
            "audienceFilter": None,
            "scheduling": {"method": "now", "timestamp": None},
        }
        router.get("/v1/campaigns", name="list_campaigns").mock(
            return_value=respx.MockResponse(200, json={"pagination": _pagination, "data": []})
        )
        router.get(url__regex=r"/v1/campaigns/[^/]+$", name="get_campaign").mock(
            return_value=respx.MockResponse(
                200,
                json={
                    "id": "mock-campaign-id",
                    "name": "Mock Campaign",
                    "status": "draft",
                    "createdAt": "2024-01-01T00:00:00.000Z",
                    "updatedAt": "2024-01-01T00:00:00.000Z",
                    "emailMessageId": None,
                    **_campaign_targeting,
                },
            )
        )
        router.post("/v1/campaigns", name="create_campaign").mock(
            return_value=respx.MockResponse(
                201,
                json={
                    "id": "mock-campaign-id",
                    "name": "Mock Campaign",
                    "status": "draft",
                    "createdAt": "2024-01-01T00:00:00.000Z",
                    "updatedAt": "2024-01-01T00:00:00.000Z",
                    "emailMessageId": "mock-email-message-id",
                    "emailMessageContentRevisionId": None,
                    **_campaign_targeting,
                },
            )
        )
        router.post(url__regex=r"/v1/campaigns/[^/]+$", name="update_campaign").mock(
            return_value=respx.MockResponse(
                200,
                json={
                    "id": "mock-campaign-id",
                    "name": "Updated Campaign",
                    "status": "draft",
                    "createdAt": "2024-01-01T00:00:00.000Z",
                    "updatedAt": "2024-01-02T00:00:00.000Z",
                    "emailMessageId": None,
                    **_campaign_targeting,
                },
            )
        )

        # Components
        router.get("/v1/components", name="list_components").mock(
            return_value=respx.MockResponse(200, json={"pagination": _pagination, "data": []})
        )
        router.get(url__regex=r"/v1/components/[^/]+$", name="get_component").mock(
            return_value=respx.MockResponse(
                200,
                json={
                    "id": "mock-component-id",
                    "name": "Mock Component",
                    "lmx": "<Text>Hello</Text>",
                },
            )
        )

        # Themes
        router.get("/v1/themes", name="list_themes").mock(
            return_value=respx.MockResponse(200, json={"pagination": _pagination, "data": []})
        )
        router.get(url__regex=r"/v1/themes/[^/]+$", name="get_theme").mock(
            return_value=respx.MockResponse(
                200,
                json={
                    "id": "mock-theme-id",
                    "name": "Mock Theme",
                    "styles": {},
                    "isDefault": False,
                    "createdAt": "2024-01-01T00:00:00.000Z",
                    "updatedAt": "2024-01-01T00:00:00.000Z",
                },
            )
        )

        # Email messages
        _email_message_json = {
            "id": "mock-email-message-id",
            "campaignId": None,
            "subject": "Mock Subject",
            "previewText": "",
            "fromName": "Test",
            "fromEmail": "test",
            "replyToEmail": "",
            "emailFormat": "styled",
            "lmx": "<Text>Hello</Text>",
            "contentRevisionId": "rev-1",
            "updatedAt": "2024-01-01T00:00:00.000Z",
        }
        router.get(url__regex=r"/v1/email-messages/[^/]+$", name="get_email_message").mock(
            return_value=respx.MockResponse(200, json=_email_message_json)
        )
        router.post(url__regex=r"/v1/email-messages/[^/]+$", name="update_email_message").mock(
            return_value=respx.MockResponse(200, json=_email_message_json)
        )

        # Contact suppression
        router.get("/v1/contacts/suppression", name="get_contact_suppression").mock(
            return_value=respx.MockResponse(
                200,
                json={
                    "contact": {"id": "mock-contact-id", "email": "user@test.com", "userId": None},
                    "isSuppressed": False,
                    "removalQuota": {"limit": 3, "used": 0, "remaining": 3},
                },
            )
        )
        router.delete("/v1/contacts/suppression", name="remove_contact_suppression").mock(
            return_value=respx.MockResponse(
                200,
                json={
                    "success": True,
                    "message": "Contact removed from suppression list.",
                    "removalQuota": {"limit": 3, "used": 1, "remaining": 2},
                },
            )
        )

        # ------------------------------------------------------------------
        # New endpoint families (Loops API v1.14.x)
        # ------------------------------------------------------------------

        # Transactional email templates
        _transactional_resource = {
            "id": "mock-transactional-id",
            "name": "Mock Transactional",
            "draftEmailMessageId": None,
            "publishedEmailMessageId": None,
            "transactionalGroupId": None,
            "createdAt": "2024-01-01T00:00:00.000Z",
            "updatedAt": "2024-01-01T00:00:00.000Z",
            "dataVariables": [],
        }
        _transactional_draft = {
            "id": "mock-transactional-id",
            "name": "Mock Transactional",
            "draftEmailMessageId": None,
            "draftEmailMessageContentRevisionId": None,
            "publishedEmailMessageId": None,
            "createdAt": "2024-01-01T00:00:00.000Z",
            "updatedAt": "2024-01-01T00:00:00.000Z",
            "dataVariables": [],
        }
        router.get("/v1/transactional-emails", name="list_transactional_templates").mock(
            return_value=respx.MockResponse(200, json={"pagination": _pagination, "data": []})
        )
        router.get(url__regex=r"/v1/transactional-emails/[^/]+$", name="get_transactional_template").mock(
            return_value=respx.MockResponse(200, json=_transactional_resource)
        )
        router.post("/v1/transactional-emails", name="create_transactional_template").mock(
            return_value=respx.MockResponse(201, json=_transactional_draft)
        )
        router.post(url__regex=r"/v1/transactional-emails/[^/]+/draft$", name="draft_transactional_template").mock(
            return_value=respx.MockResponse(200, json=_transactional_draft)
        )
        router.post(url__regex=r"/v1/transactional-emails/[^/]+/publish$", name="publish_transactional_template").mock(
            return_value=respx.MockResponse(200, json=_transactional_resource)
        )
        router.post(url__regex=r"/v1/transactional-emails/[^/]+$", name="update_transactional_template").mock(
            return_value=respx.MockResponse(200, json=_transactional_resource)
        )

        # Uploads
        router.post("/v1/uploads", name="create_upload").mock(
            return_value=respx.MockResponse(
                200,
                json={"emailAssetId": "mock-asset-id", "presignedUrl": "https://example.com/upload"},
            )
        )
        router.post(url__regex=r"/v1/uploads/[^/]+/complete$", name="complete_upload").mock(
            return_value=respx.MockResponse(
                200,
                json={"emailAssetId": "mock-asset-id", "finalUrl": "https://example.com/final.png"},
            )
        )

        # Workflows
        router.get("/v1/workflows", name="list_workflows").mock(
            return_value=respx.MockResponse(200, json={"pagination": _pagination, "data": []})
        )
        router.get(url__regex=r"/v1/workflows/[^/]+/nodes/[^/]+$", name="get_workflow_node").mock(
            return_value=respx.MockResponse(
                200,
                json={
                    "id": "mock-node-id",
                    "workflowId": "mock-workflow-id",
                    "typeName": "ExitAction",
                    "nextNodeIds": [],
                },
            )
        )
        router.get(url__regex=r"/v1/workflows/[^/]+$", name="get_workflow").mock(
            return_value=respx.MockResponse(
                200,
                json={"id": "mock-workflow-id", "rootNodeId": "mock-node-id", "nodes": {}},
            )
        )

        # Audience segments
        router.get("/v1/audience-segments", name="list_audience_segments").mock(
            return_value=respx.MockResponse(200, json={"pagination": _pagination, "data": []})
        )
        router.get(url__regex=r"/v1/audience-segments/[^/]+$", name="get_audience_segment").mock(
            return_value=respx.MockResponse(
                200,
                json={
                    "id": "mock-segment-id",
                    "name": "Mock Segment",
                    "description": "A mock audience segment",
                    "createdAt": "2024-01-01T00:00:00.000Z",
                    "updatedAt": "2024-01-01T00:00:00.000Z",
                    "filter": None,
                },
            )
        )

        # Campaign + transactional groups (shared GroupResponse shape)
        _group_json = {
            "id": "mock-group-id",
            "name": "Mock Group",
            "description": "A mock group",
            "createdAt": "2024-01-01T00:00:00.000Z",
            "updatedAt": "2024-01-01T00:00:00.000Z",
        }
        router.get("/v1/campaign-groups", name="list_campaign_groups").mock(
            return_value=respx.MockResponse(200, json={"pagination": _pagination, "data": []})
        )
        router.get(url__regex=r"/v1/campaign-groups/[^/]+$", name="get_campaign_group").mock(
            return_value=respx.MockResponse(200, json=_group_json)
        )
        router.post("/v1/campaign-groups", name="create_campaign_group").mock(
            return_value=respx.MockResponse(200, json=_group_json)
        )
        router.post(url__regex=r"/v1/campaign-groups/[^/]+$", name="update_campaign_group").mock(
            return_value=respx.MockResponse(200, json=_group_json)
        )
        router.get("/v1/transactional-groups", name="list_transactional_groups").mock(
            return_value=respx.MockResponse(200, json={"pagination": _pagination, "data": []})
        )
        router.get(url__regex=r"/v1/transactional-groups/[^/]+$", name="get_transactional_group").mock(
            return_value=respx.MockResponse(200, json=_group_json)
        )
        router.post("/v1/transactional-groups", name="create_transactional_group").mock(
            return_value=respx.MockResponse(200, json=_group_json)
        )
        router.post(url__regex=r"/v1/transactional-groups/[^/]+$", name="update_transactional_group").mock(
            return_value=respx.MockResponse(200, json=_group_json)
        )

        # Email message preview
        router.post(url__regex=r"/v1/email-messages/[^/]+/preview$", name="preview_email_message").mock(
            return_value=respx.MockResponse(200, json={"id": "mock-preview-id"})
        )

        try:
            yield router
        finally:
            pyloops.reset_client()
