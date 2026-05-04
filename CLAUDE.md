# pyloops

Unofficial Python SDK for [Loops.so](https://loops.so) — an email marketing and transactional email platform. The library wraps the Loops REST API and is published to PyPI as `pyloops`.

## Architecture

Two layers:

**High-level API** (`src/pyloops/client.py`) — `LoopsClient` wraps every Loops endpoint with Pythonic method signatures, proper error handling, and safe mode. This is what consumers use. The module-level `get_client()` / `reset_client()` / `configure()` functions manage a singleton instance.

**Low-level API** (`src/pyloops/_generated/`) — auto-generated from the Loops OpenAPI spec using `openapi-python-client`. Never edit this directory by hand; it is regenerated on each SDK version bump. The generated code is excluded from ruff linting.

Supporting modules:
- `src/pyloops/config.py` — global config (`configure()`, `get_config()`), reads `LOOPS_API_KEY` env var
- `src/pyloops/exceptions.py` — exception hierarchy (`LoopsError`, `LoopsRateLimitError`, `LoopsContactExistsError`, `LoopsUnsafeEmailError`, `LoopsConfigurationError`)
- `src/pyloops/responses.py` — hand-written response models for endpoints where the generated model is insufficient (e.g. `TransactionalEmailsResponse`)
- `src/pyloops/testing.py` — testing utilities (see below)

## SDK version bump workflow

When Loops releases a new API version:
1. Regenerate `src/pyloops/_generated/` from the updated OpenAPI spec
2. Identify new endpoints by diffing the generated `api/` and `models/` directories
3. Add wrapper methods to `LoopsClient` in `client.py` following existing patterns
4. Add mock routes to `loops_respx_mock()` in `testing.py`
5. Add tests to `tests/test_testing.py`
6. Bump the version in `pyproject.toml`

## Testing strategy

Tests run with pytest and require no real API key — all HTTP is intercepted at the httpx transport level by `respx`.

```
tests/
  test_safe_mode.py   # 40 tests — safe mode email domain validation
  test_testing.py     # 31 tests — mock utility + every client method
```

Run tests:
```bash
python -m pytest tests/ -v
```

Format code (run before committing):
```bash
uv run ruff format .
```

### test_safe_mode.py

Covers the safe mode feature: when enabled, the client raises `LoopsUnsafeEmailError` for any email whose domain is not in `safe_mode_allowed_domains`. Tests are parametrized across blocked domains (`@gmail.com`, `@company.io`, `@loops.so`) and allowed domains. Also covers:
- `user_id`-only calls skip email validation entirely
- `configure()` + `get_config()` round-trip
- Singleton lifecycle when safe mode config changes
- `loops_respx_mock()` defaults to safe mode off

### test_testing.py

Covers every public `LoopsClient` method with happy-path and error-simulation tests:
- **Happy path** — every client method called against the mock, result type and key fields asserted
- **Request body inspection** — verify camelCase serialisation, UNSET fields omitted from payload
- **Error simulation** — 400 and 404 failures assert `LoopsError` with the right message; 429 asserts `LoopsRateLimitError` with correct `limit`/`remaining` values
- **Input validation** — methods that require `email` or `user_id` raise `LoopsError` before any HTTP call
- **Mock lifecycle** — singleton reset on enter/exit, custom API key propagated to `Authorization` header, unregistered routes raise immediately
- **Named route completeness** — `test_named_routes_accessible` asserts every route in `EXPECTED_ROUTE_NAMES` exists

When adding a new client method, add: one happy-path test, one error test (400 or 404), and a 429 rate-limit test if the endpoint is frequently called.

## Testing module (`pyloops.testing`)

Install the extra: `pip install pyloops[testing]` (adds `respx`).

### Basic usage

```python
import json
import pyloops
from pyloops.testing import loops_respx_mock

async def test_something():
    with loops_respx_mock() as api:
        client = pyloops.get_client()
        result = await client.send_transactional_email(
            transactional_id="tpl_abc",
            email="user@test.com",
        )
        assert result.success is True

        # Inspect what pyloops actually sent over the wire
        body = json.loads(api["transactional"].calls[0].request.content)
        assert body["transactionalId"] == "tpl_abc"
```

### What it does

`loops_respx_mock()` is a context manager that:
1. Calls `pyloops.configure()` with the given `api_key` (default `"test-key"`)
2. Resets the singleton client so a fresh one is created against the mock
3. Activates a `respx` router that intercepts all httpx calls to `https://app.loops.so/api/v1`
4. Registers a default success response for every Loops endpoint
5. On exit, resets the singleton again to prevent state leaking between tests

All routes are accessible by name on the yielded router.

### Named routes

| Name | Endpoint |
|---|---|
| `health` | `GET /api-key` |
| `create_contact` | `POST /contacts/create` |
| `upsert_contact` | `PUT /contacts/update` |
| `find_contact` | `GET /contacts/find` |
| `delete_contact` | `POST /contacts/delete` |
| `list_contact_properties` | `GET /contacts/properties` |
| `create_contact_property` | `POST /contacts/properties` |
| `get_contact_suppression` | `GET /contacts/suppression` |
| `remove_contact_suppression` | `DELETE /contacts/suppression` |
| `send_event` | `POST /events/send` |
| `list_mailing_lists` | `GET /lists` |
| `transactional` | `POST /transactional` |
| `list_transactional` | `GET /transactional` |
| `list_sending_ips` | `GET /dedicated-sending-ips` |
| `list_campaigns` | `GET /campaigns` |
| `create_campaign` | `POST /campaigns` |
| `get_campaign` | `GET /campaigns/{id}` |
| `update_campaign` | `POST /campaigns/{id}` |
| `list_components` | `GET /components` |
| `get_component` | `GET /components/{id}` |
| `list_themes` | `GET /themes` |
| `get_theme` | `GET /themes/{id}` |
| `get_email_message` | `GET /email-messages/{id}` |
| `update_email_message` | `POST /email-messages/{id}` |

### Simulating errors

Override any named route before calling the client:

```python
from httpx import Response
from pyloops.exceptions import LoopsRateLimitError

async def test_rate_limit():
    with loops_respx_mock() as api:
        api["transactional"].mock(return_value=Response(
            429,
            json={"success": False},
            headers={"x-ratelimit-limit": "10", "x-ratelimit-remaining": "0"},
        ))
        client = pyloops.get_client()
        with pytest.raises(LoopsRateLimitError) as exc_info:
            await client.send_transactional_email(transactional_id="x", email="u@test.com")
        assert exc_info.value.limit == 10
```

### Safe mode in tests

```python
with loops_respx_mock(safe_mode=True, safe_mode_allowed_domains=("@mycompany.com",)) as api:
    client = pyloops.get_client()
    # emails not ending in @mycompany.com will raise LoopsUnsafeEmailError
```

### Recommended pytest fixture

```python
import pytest
from pyloops.testing import loops_respx_mock

@pytest.fixture
def loops_api():
    with loops_respx_mock() as router:
        yield router
```
