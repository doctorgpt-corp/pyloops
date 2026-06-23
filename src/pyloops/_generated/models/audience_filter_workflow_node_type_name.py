from enum import Enum


class AudienceFilterWorkflowNodeTypeName(str, Enum):
    AUDIENCEFILTER = "AudienceFilter"

    def __str__(self) -> str:
        return str(self.value)
