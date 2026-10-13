from enum import StrEnum


class SimplifiedAddToListTriggerWorkflowNodeTypeName(StrEnum):
    ADDTOLISTTRIGGER = "AddToListTrigger"

    def __str__(self) -> str:
        return str(self.value)
