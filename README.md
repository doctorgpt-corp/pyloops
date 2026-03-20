# PyLoops

Unofficial Python SDK for [Loops.so](https://loops.so).

[![PyPI version](https://badge.fury.io/py/pyloops.svg)](https://badge.fury.io/py/pyloops)
[![Python 3.12+](https://img.shields.io/badge/python-3.12+-blue.svg)](https://www.python.org/downloads/)

## Installation

```bash
pip install pyloops
```

Or with uv:

```bash
uv add pyloops
```

## Quick Start

PyLoops offers two ways to interact with the Loops API:

### High-Level API

```python
import pyloops

# Configure once (or set LOOPS_API_KEY environment variable)
pyloops.configure(api_key="your_api_key_here")

# Get the client
client = pyloops.get_client()

# Upsert a contact
await client.upsert_contact(
    email="user@example.com",
    first_name="John",
    last_name="Doe",
    subscribed=True,
)

# Find a contact
contacts = await client.find_contact(email="user@example.com")

# Send an event
await client.send_event(
    event_name="user_signup",
    email="user@example.com",
    event_properties={"plan": "premium"},
)

# List mailing lists
mailing_lists = await client.list_mailing_lists()
```

### Low-Level API

For more control, use the auto-generated low-level API directly:

```python
from pyloops import AuthenticatedClient
from pyloops.api.contacts import put_contacts_update
from pyloops.models import ContactUpdateRequest

client = AuthenticatedClient(
    base_url="https://app.loops.so/api/v1",
    token="your_api_key_here",
)

response = await put_contacts_update.asyncio(
    client=client,
    body=ContactUpdateRequest(
        email="user@example.com",
        first_name="John",
        last_name="Doe"
    )
)
```

## Authentication

All API calls require a Loops API key. Get your API key from your [Loops account settings](https://app.loops.so/settings).

There are three ways to configure authentication:

1. **Environment variable**:
```bash
export LOOPS_API_KEY="your_api_key_here"
```

2. **Module-level configuration**:
```python
import pyloops
pyloops.configure(api_key="your_api_key_here")
```

3. **Per-client configuration**:
```python
import pyloops
client = pyloops.LoopsClient(api_key="your_api_key_here")
```

## Features

This SDK provides access to all Loops.so API endpoints:

- **Contacts**: Create, update, find, and delete contacts
- **Contact Properties**: Manage custom contact properties
- **Mailing Lists**: View available mailing lists
- **Events**: Trigger event-based emails
- **Transactional Emails**: Send and list transactional emails
- **Sending IPs**: Retrieve dedicated sending IP addresses

## Safe Mode

When developing locally, you can enable **safe mode** to prevent accidentally sending emails or syncing contacts to real addresses. With safe mode enabled, only emails matching your allowed domains will be accepted — all others will raise a `LoopsUnsafeEmailError`.

```python
import pyloops

pyloops.configure(
    api_key="your_api_key_here",
    safe_mode=True,
    safe_mode_allowed_domains=("@test.com", "@example.com", "@yourcompany.com"),
)

client = pyloops.get_client()

# This works
await client.send_transactional_email(
    transactional_id="welcome",
    email="dev@test.com",
)

# This raises LoopsUnsafeEmailError
await client.send_transactional_email(
    transactional_id="welcome",
    email="real-user@gmail.com",
)
```

You can also set it per-client:

```python
client = pyloops.LoopsClient(
    api_key="your_api_key_here",
    safe_mode=True,
    safe_mode_allowed_domains=("@test.com",),
)
```

## Testing

PyLoops ships a testing module that mocks all Loops API endpoints at the HTTP transport level using [respx](https://lundberg.github.io/respx/). Your real client code runs end-to-end, but no actual API requests leave the process.

Install with the `testing` extra:

```bash
pip install pyloops[testing]
```

### Basic usage

```python
import json
import pyloops
from pyloops.testing import loops_respx_mock

async def test_sends_welcome_email():
    with loops_respx_mock() as api:
        client = pyloops.get_client()
        await client.send_transactional_email(
            transactional_id="welcome",
            email="user@test.com",
            data_variables={"name": "Jan"},
        )

        # Inspect the HTTP request that pyloops made
        request = api["transactional"].calls[0].request
        body = json.loads(request.content)
        assert body["transactionalId"] == "welcome"
        assert body["email"] == "user@test.com"
```

### Pytest fixture

```python
import pytest
from pyloops.testing import loops_respx_mock

@pytest.fixture
def loops_api():
    with loops_respx_mock() as router:
        yield router

async def test_create_contact(loops_api):
    client = pyloops.get_client()
    result = await client.create_contact(email="new@test.com")
    assert result.success is True
    assert loops_api["create_contact"].called
```

### Simulating errors

Override any route to return custom responses:

```python
from httpx import Response

async def test_handles_rate_limit(loops_api):
    loops_api["transactional"].mock(
        return_value=Response(
            429,
            json={"success": False},
            headers={"x-ratelimit-limit": "10", "x-ratelimit-remaining": "0"},
        )
    )
    client = pyloops.get_client()
    with pytest.raises(pyloops.LoopsRateLimitError):
        await client.send_transactional_email(transactional_id="abc", email="user@test.com")
```

### Available mock routes

All routes are accessible by name on the yielded router:

| Name | Method | Endpoint |
|------|--------|----------|
| `health` | GET | `/api-key` |
| `transactional` | POST | `/transactional` |
| `list_transactional` | GET | `/transactional` |
| `create_contact` | POST | `/contacts/create` |
| `upsert_contact` | PUT | `/contacts/update` |
| `find_contact` | GET | `/contacts/find` |
| `delete_contact` | POST | `/contacts/delete` |
| `list_contact_properties` | GET | `/contacts/properties` |
| `create_contact_property` | POST | `/contacts/properties` |
| `send_event` | POST | `/events/send` |
| `list_mailing_lists` | GET | `/lists` |
| `list_sending_ips` | GET | `/dedicated-sending-ips` |

### Testing with safe mode

The mock disables safe mode by default. To test safe mode behavior, pass `safe_mode=True` and your allowed domains:

```python
with loops_respx_mock(safe_mode=True, safe_mode_allowed_domains=("@test.com",)) as api:
    client = pyloops.get_client()
    await client.send_transactional_email(transactional_id="t1", email="dev@test.com")  # OK
    await client.send_transactional_email(transactional_id="t1", email="user@gmail.com")  # raises
```

## Documentation

For detailed API documentation, visit the [Loops.so API docs](https://loops.so/docs).

## Automated Updates

This SDK is automatically updated to match the latest Loops.so API specification. The package version corresponds to the Loops API version (current: **1.7.0**).

A GitHub Action checks for API updates daily and creates a pull request when changes are detected. After review and merge, a new version is automatically published to PyPI.

## Development

### Setup

```bash
# Clone the repository
git clone https://github.com/doctorgpt-corp/pyloops.git
cd pyloops

# Install dependencies with uv
uv sync --all-groups
```

### Running Tests

Using `just`:

```bash
just check      # Run linting + type checking
just lint       # Run linting only
just typecheck  # Run type checking only
just fmt        # Format code
```

Or directly with `uv`:

```bash
uv run ruff check src/
uv run pyright src/
```

### Project Structure

```
src/pyloops/
├── __init__.py          # Main exports
├── client.py            # High-level LoopsClient wrapper
├── config.py            # Configuration
├── exceptions.py        # Exceptions
├── api/                 # Re-exports from _generated.api
├── models/              # Re-exports from _generated.models
└── _generated/          # ALL auto-generated code
    ├── client.py
    ├── api/
    ├── models/
    └── types.py
```

### Regenerate SDK

To manually regenerate the SDK from the latest OpenAPI spec:

```bash
just generate
```

Or manually:

```bash
rm -rf src/pyloops/_generated
uv tool run openapi-python-client generate --url https://app.loops.so/openapi.yaml --meta uv
mv loops-open-api-spec-client/loops_open_api_spec_client src/pyloops/_generated
rm -rf loops-open-api-spec-client openapi.yaml
```

Custom code is never touched during regeneration.

## License

MIT

## Disclaimer

This is an unofficial SDK and is not affiliated with or endorsed by Loops.so.
