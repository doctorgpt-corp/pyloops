from enum import StrEnum


class SimplifiedBlankTriggerWorkflowNodeTypeName(StrEnum):
    BLANKTRIGGER = "BlankTrigger"

    def __str__(self) -> str:
        return str(self.value)
