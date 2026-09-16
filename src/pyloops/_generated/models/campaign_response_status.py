from enum import StrEnum


class CampaignResponseStatus(StrEnum):
    DRAFT = "Draft"
    SCHEDULED = "Scheduled"
    SENDING = "Sending"
    SENT = "Sent"

    def __str__(self) -> str:
        return str(self.value)
