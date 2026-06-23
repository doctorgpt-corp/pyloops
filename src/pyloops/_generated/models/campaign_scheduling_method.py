from enum import Enum


class CampaignSchedulingMethod(str, Enum):
    NOW = "now"
    SCHEDULE = "schedule"

    def __str__(self) -> str:
        return str(self.value)
