from pyloops._generated.client import AuthenticatedClient, Client
from pyloops.client import LoopsClient, get_client
from pyloops.config import configure, get_config
from pyloops.exceptions import (
    LoopsConfigurationError,
    LoopsContactExistsError,
    LoopsError,
    LoopsRateLimitError,
)
from pyloops.responses import (
    TransactionalEmail,
    TransactionalEmailPagination,
    TransactionalEmailsResponse,
)

__all__ = (
    # High-level API
    "LoopsClient",
    "get_client",
    "configure",
    "get_config",
    "LoopsError",
    "LoopsConfigurationError",
    "LoopsContactExistsError",
    "LoopsRateLimitError",
    # Response models
    "TransactionalEmail",
    "TransactionalEmailPagination",
    "TransactionalEmailsResponse",
    # Low-level API
    "AuthenticatedClient",
    "Client",
)
