from enum import StrEnum


class CampaignListItemStatus(StrEnum):
    DRAFT = "Draft"
    SCHEDULED = "Scheduled"
    SENDING = "Sending"
    SENT = "Sent"

    def __str__(self) -> str:
        return str(self.value)
