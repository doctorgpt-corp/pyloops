from enum import StrEnum


class AudienceFilterWorkflowNodeTypeName(StrEnum):
    AUDIENCEFILTER = "AudienceFilter"

    def __str__(self) -> str:
        return str(self.value)
