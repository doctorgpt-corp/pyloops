from enum import Enum


class BlankTriggerWorkflowNodeTypeName(str, Enum):
    BLANKTRIGGER = "BlankTrigger"

    def __str__(self) -> str:
        return str(self.value)
