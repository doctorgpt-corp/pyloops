from enum import StrEnum


class CampaignSchedulingMethod(StrEnum):
    NOW = "now"
    SCHEDULE = "schedule"

    def __str__(self) -> str:
        return str(self.value)
