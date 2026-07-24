from enum import Enum


class CampaignResponseStatus(str, Enum):
    DRAFT = "Draft"
    SCHEDULED = "Scheduled"
    SENDING = "Sending"
    SENT = "Sent"

    def __str__(self) -> str:
        return str(self.value)
