from enum import StrEnum


class CampaignSchedulingRequestMethod(StrEnum):
    NOW = "now"
    SCHEDULE = "schedule"

    def __str__(self) -> str:
        return str(self.value)
