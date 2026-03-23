"""Tests for safe_mode email domain validation."""

import pytest

import pyloops
from pyloops import LoopsClient
from pyloops.exceptions import LoopsConfigurationError, LoopsUnsafeEmailError
from pyloops.testing import loops_respx_mock

ALLOWED_DOMAINS = ("@test.com", "@example.com", "@mycompany.io")


@pytest.fixture
def safe_client():
    with loops_respx_mock(safe_mode=True, safe_mode_allowed_domains=ALLOWED_DOMAINS):
        yield pyloops.get_client()


# ---------------------------------------------------------------------------
# Blocked emails
# ---------------------------------------------------------------------------

UNSAFE_EMAILS = [
    "user@gmail.com",
    "user@company.io",
    "user@loops.so",
]


@pytest.mark.asyncio
@pytest.mark.parametrize("email", UNSAFE_EMAILS)
async def test_send_transactional_email_blocked(safe_client, email):
    with pytest.raises(LoopsUnsafeEmailError):
        await safe_client.send_transactional_email(transactional_id="tpl_1", email=email)


@pytest.mark.asyncio
@pytest.mark.parametrize("email", UNSAFE_EMAILS)
async def test_create_contact_blocked(safe_client, email):
    with pytest.raises(LoopsUnsafeEmailError):
        await safe_client.create_contact(email=email)


@pytest.mark.asyncio
@pytest.mark.parametrize("email", UNSAFE_EMAILS)
async def test_upsert_contact_blocked(safe_client, email):
    with pytest.raises(LoopsUnsafeEmailError):
        await safe_client.upsert_contact(email=email)


@pytest.mark.asyncio
@pytest.mark.parametrize("email", UNSAFE_EMAILS)
async def test_find_contact_blocked(safe_client, email):
    with pytest.raises(LoopsUnsafeEmailError):
        await safe_client.find_contact(email=email)


@pytest.mark.asyncio
@pytest.mark.parametrize("email", UNSAFE_EMAILS)
async def test_delete_contact_blocked(safe_client, email):
    with pytest.raises(LoopsUnsafeEmailError):
        await safe_client.delete_contact(email=email)


@pytest.mark.asyncio
@pytest.mark.parametrize("email", UNSAFE_EMAILS)
async def test_send_event_blocked(safe_client, email):
    with pytest.raises(LoopsUnsafeEmailError):
        await safe_client.send_event(event_name="signup", email=email)


# ---------------------------------------------------------------------------
# Allowed emails
# ---------------------------------------------------------------------------

ALLOWED_EMAILS = [
    "dev@test.com",
    "dev@example.com",
    "dev@mycompany.io",
    "DEV@MYCOMPANY.IO",  # case insensitive
]


@pytest.mark.asyncio
@pytest.mark.parametrize("email", ALLOWED_EMAILS)
async def test_send_transactional_email_allowed(safe_client, email):
    result = await safe_client.send_transactional_email(transactional_id="tpl_1", email=email)
    assert result.success is True


@pytest.mark.asyncio
@pytest.mark.parametrize("email", ALLOWED_EMAILS)
async def test_create_contact_allowed(safe_client, email):
    result = await safe_client.create_contact(email=email)
    assert result.success is True


@pytest.mark.asyncio
@pytest.mark.parametrize("email", ALLOWED_EMAILS)
async def test_send_event_allowed(safe_client, email):
    result = await safe_client.send_event(event_name="signup", email=email)
    assert result.success is True


# ---------------------------------------------------------------------------
# Safe mode off (default) — no restrictions
# ---------------------------------------------------------------------------


@pytest.mark.asyncio
async def test_safe_mode_off_allows_any_email():
    with loops_respx_mock():
        client = LoopsClient(api_key="test-key", safe_mode=False)
        result = await client.send_transactional_email(transactional_id="tpl_1", email="user@gmail.com")
        assert result.success is True


# ---------------------------------------------------------------------------
# No email provided — should not raise
# ---------------------------------------------------------------------------


@pytest.mark.asyncio
async def test_upsert_by_user_id_skips_validation(safe_client):
    result = await safe_client.upsert_contact(user_id="usr_123", first_name="Test")
    assert result.success is True


@pytest.mark.asyncio
async def test_send_event_by_user_id_skips_validation(safe_client):
    result = await safe_client.send_event(event_name="signup", user_id="usr_123")
    assert result.success is True


# ---------------------------------------------------------------------------
# configure() / get_client() flow
# ---------------------------------------------------------------------------


def test_configure_safe_mode_reflected_in_get_config():
    pyloops.configure(safe_mode=True, safe_mode_allowed_domains=("@dev.com",))
    config = pyloops.get_config()
    assert config["safe_mode"] is True
    assert config["safe_mode_allowed_domains"] == ("@dev.com",)
    pyloops.configure(safe_mode=False, safe_mode_allowed_domains=())


@pytest.mark.asyncio
async def test_get_client_picks_up_configured_safe_mode():
    with loops_respx_mock(safe_mode=True, safe_mode_allowed_domains=("@test.com",)):
        client = pyloops.get_client()
        with pytest.raises(LoopsUnsafeEmailError):
            await client.send_transactional_email(transactional_id="tpl_1", email="user@gmail.com")


@pytest.mark.asyncio
async def test_reset_client_picks_up_changed_safe_mode():
    with loops_respx_mock(safe_mode=False):
        client = pyloops.get_client()
        result = await client.send_transactional_email(transactional_id="tpl_1", email="user@gmail.com")
        assert result.success is True

        # Now enable safe mode and reset the singleton
        pyloops.configure(safe_mode=True, safe_mode_allowed_domains=("@test.com",))
        pyloops.reset_client()
        client = pyloops.get_client()
        with pytest.raises(LoopsUnsafeEmailError):
            await client.send_transactional_email(transactional_id="tpl_1", email="user@gmail.com")


@pytest.mark.asyncio
async def test_loops_respx_mock_defaults_to_safe_mode_off():
    with loops_respx_mock():
        client = pyloops.get_client()
        result = await client.send_transactional_email(transactional_id="tpl_1", email="user@gmail.com")
        assert result.success is True


@pytest.mark.asyncio
async def test_explicit_safe_mode_overrides_config():
    """safe_mode passed directly to LoopsClient takes precedence over configure()."""
    with loops_respx_mock(safe_mode=False):
        client = LoopsClient(
            api_key="test-key",
            safe_mode=True,
            safe_mode_allowed_domains=("@test.com",),
        )
        with pytest.raises(LoopsUnsafeEmailError):
            await client.send_transactional_email(transactional_id="tpl_1", email="user@gmail.com")


# ---------------------------------------------------------------------------
# safe_mode=True without allowed domains
# ---------------------------------------------------------------------------


@pytest.mark.asyncio
async def test_safe_mode_without_domains_raises_configuration_error():
    """Enabling safe_mode without specifying allowed domains should raise."""
    with loops_respx_mock(safe_mode=True, safe_mode_allowed_domains=()):
        client = pyloops.get_client()
        with pytest.raises(LoopsConfigurationError, match="no safe_mode_allowed_domains"):
            await client.send_transactional_email(transactional_id="tpl_1", email="user@test.com")


# ---------------------------------------------------------------------------
# Custom domains
# ---------------------------------------------------------------------------


@pytest.mark.asyncio
async def test_custom_allowed_domains():
    """Users can configure their own allowed domains."""
    with loops_respx_mock(safe_mode=True, safe_mode_allowed_domains=("@acme.dev",)):
        client = pyloops.get_client()
        result = await client.send_transactional_email(transactional_id="tpl_1", email="dev@acme.dev")
        assert result.success is True

        with pytest.raises(LoopsUnsafeEmailError):
            await client.send_transactional_email(transactional_id="tpl_1", email="dev@test.com")
