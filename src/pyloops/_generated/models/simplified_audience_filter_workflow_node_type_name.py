from enum import StrEnum


class SimplifiedAudienceFilterWorkflowNodeTypeName(StrEnum):
    AUDIENCEFILTER = "AudienceFilter"

    def __str__(self) -> str:
        return str(self.value)
