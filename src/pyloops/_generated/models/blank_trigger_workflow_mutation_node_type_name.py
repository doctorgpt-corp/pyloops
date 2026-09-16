from enum import StrEnum


class BlankTriggerWorkflowMutationNodeTypeName(StrEnum):
    BLANKTRIGGER = "BlankTrigger"

    def __str__(self) -> str:
        return str(self.value)
