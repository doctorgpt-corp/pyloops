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

BASE_URL = "https://app.loops.so/api/v1"


@contextmanager
def loops_respx_mock(
    *,
    api_key: str = "test-key",
    base_url: str = BASE_URL,
    assert_all_mocked: bool = True,
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
    """
    pyloops.configure(api_key=api_key, base_url=base_url)
    pyloops.reset_client()
    with respx.mock(base_url=base_url, assert_all_called=False, assert_all_mocked=assert_all_mocked) as router:
        # Health / API key validation
        router.get("/api-key", name="health").mock(
            return_value=respx.MockResponse(200, json={"success": True, "teamName": "Test"})
        )

        # Transactional emails
        router.post("/transactional", name="transactional").mock(
            return_value=respx.MockResponse(200, json={"success": True})
        )
        router.get("/transactional", name="list_transactional").mock(
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
        router.post("/contacts/create", name="create_contact").mock(
            return_value=respx.MockResponse(200, json={"success": True, "id": "mock-contact-id"})
        )
        router.put("/contacts/update", name="upsert_contact").mock(
            return_value=respx.MockResponse(200, json={"success": True, "id": "mock-contact-id"})
        )
        router.get("/contacts/find", name="find_contact").mock(
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
        router.post("/contacts/delete", name="delete_contact").mock(
            return_value=respx.MockResponse(200, json={"message": "Contact deleted.", "success": True})
        )

        # Contact properties
        router.get("/contacts/properties", name="list_contact_properties").mock(
            return_value=respx.MockResponse(200, json=[])
        )
        router.post("/contacts/properties", name="create_contact_property").mock(
            return_value=respx.MockResponse(200, json={"key": "custom_prop", "label": "Custom Prop", "type": "string"})
        )

        # Events
        router.post("/events/send", name="send_event").mock(
            return_value=respx.MockResponse(200, json={"success": True})
        )

        # Mailing lists
        router.get("/lists", name="list_mailing_lists").mock(return_value=respx.MockResponse(200, json=[]))

        # Dedicated sending IPs
        router.get("/dedicated-sending-ips", name="list_sending_ips").mock(
            return_value=respx.MockResponse(200, json=[])
        )

        try:
            yield router
        finally:
            pyloops.reset_client()
