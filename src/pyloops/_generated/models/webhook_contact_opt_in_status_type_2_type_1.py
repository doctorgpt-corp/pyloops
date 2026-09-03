from enum import StrEnum


class WebhookContactOptInStatusType2Type1(StrEnum):
    ACCEPTED = "accepted"
    PENDING = "pending"
    REJECTED = "rejected"

    def __str__(self) -> str:
        return str(self.value)
