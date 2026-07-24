from enum import Enum


class AudienceFilterWorkflowMutationNodeTypeName(str, Enum):
    AUDIENCEFILTER = "AudienceFilter"

    def __str__(self) -> str:
        return str(self.value)
