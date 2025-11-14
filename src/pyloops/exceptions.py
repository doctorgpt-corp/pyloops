from typing import Any


class LoopsError(Exception):
    """Base exception for Loops API errors."""

    def __init__(
        self,
        message: str,
        status_code: int | None = None,
        response_data: Any = None,
    ):
        """
        Initialize a LoopsError.

        Args:
            message: Error message describing what went wrong
            status_code: HTTP status code if available
            response_data: Raw response data from the API
        """
        self.message = message
        self.status_code = status_code
        self.response_data = response_data
        super().__init__(message)

    def __str__(self) -> str:
        if self.status_code:
            return f"[{self.status_code}] {self.message}"
        return self.message


class LoopsConfigurationError(LoopsError):
    def __init__(self, message: str = "API key not configured"):
        super().__init__(message, status_code=None)


class LoopsRateLimitError(LoopsError):
    def __init__(
        self,
        message: str = "Rate limit exceeded",
        limit: int | None = None,
        remaining: int | None = None,
    ):
        self.limit = limit
        self.remaining = remaining
        super().__init__(message, status_code=429)
