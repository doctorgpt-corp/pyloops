from enum import Enum


class SimplifiedAudienceFilterWorkflowNodeTypeName(str, Enum):
    AUDIENCEFILTER = "AudienceFilter"

    def __str__(self) -> str:
        return str(self.value)
