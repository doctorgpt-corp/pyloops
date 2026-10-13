from enum import StrEnum


class BlankTriggerWorkflowNodeTypeName(StrEnum):
    BLANKTRIGGER = "BlankTrigger"

    def __str__(self) -> str:
        return str(self.value)
