from enum import Enum


class SimplifiedBlankTriggerWorkflowNodeTypeName(str, Enum):
    BLANKTRIGGER = "BlankTrigger"

    def __str__(self) -> str:
        return str(self.value)
