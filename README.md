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

```python
from pyloops import Client

# Initialize the client with your API key
client = Client(base_url="https://app.loops.so/api/v1", token="your_api_key_here")

# Create a contact
from pyloops.api.contacts import create_contact
from pyloops.models import CreateContactBody

response = create_contact.sync(
    client=client,
    body=CreateContactBody(
        email="user@example.com",
        first_name="John",
        last_name="Doe"
    )
)

print(response)
```

## Authentication

All API calls require a Loops API key. Get your API key from your [Loops account settings](https://app.loops.so/settings).

```python
from pyloops import Client

client = Client(
    base_url="https://app.loops.so/api/v1",
    token="your_api_key_here"
)
```

## Features

This SDK provides access to all Loops.so API endpoints:

- **Contacts**: Create, update, find, and delete contacts
- **Contact Properties**: Manage custom contact properties
- **Mailing Lists**: View available mailing lists
- **Events**: Trigger event-based emails
- **Transactional Emails**: Send and list transactional emails
- **Sending IPs**: Retrieve dedicated sending IP addresses

## Documentation

For detailed API documentation, visit the [Loops.so API docs](https://loops.so/docs).

## Automated Updates

This SDK is automatically updated to match the latest Loops.so API specification. The package version corresponds to the Loops API version (current: **1.6.0**).

A GitHub Action checks for API updates daily and creates a pull request when changes are detected. After review and merge, a new version is automatically published to PyPI.

## Development

### Setup

```bash
# Clone the repository
git clone https://github.com/doctorgpt-corp/pyloops.git
cd pyloops

# Install dependencies with uv
uv sync
```

### Regenerate SDK

To manually regenerate the SDK from the latest OpenAPI spec:

```bash
uv run openapi-python-client generate --url https://app.loops.so/openapi.yaml --meta uv
cp -r loops-open-api-spec-client/loops_open_api_spec_client/* src/pyloops/
rm -rf loops-open-api-spec-client
```

## License

MIT

## Disclaimer

This is an unofficial SDK and is not affiliated with or endorsed by Loops.so.
