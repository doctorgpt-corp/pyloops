from enum import StrEnum


class AddToListTriggerWorkflowNodeTypeName(StrEnum):
    ADDTOLISTTRIGGER = "AddToListTrigger"

    def __str__(self) -> str:
        return str(self.value)
