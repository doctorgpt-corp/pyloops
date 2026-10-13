from enum import StrEnum


class AudienceFilterWorkflowMutationNodeTypeName(StrEnum):
    AUDIENCEFILTER = "AudienceFilter"

    def __str__(self) -> str:
        return str(self.value)
