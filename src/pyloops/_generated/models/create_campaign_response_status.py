from enum import StrEnum


class CreateCampaignResponseStatus(StrEnum):
    DRAFT = "Draft"

    def __str__(self) -> str:
        return str(self.value)
