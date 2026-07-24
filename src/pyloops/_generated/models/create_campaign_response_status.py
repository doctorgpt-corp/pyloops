from enum import Enum


class CreateCampaignResponseStatus(str, Enum):
    DRAFT = "Draft"

    def __str__(self) -> str:
        return str(self.value)
