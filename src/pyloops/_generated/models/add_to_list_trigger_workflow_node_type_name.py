from enum import Enum


class AddToListTriggerWorkflowNodeTypeName(str, Enum):
    ADDTOLISTTRIGGER = "AddToListTrigger"

    def __str__(self) -> str:
        return str(self.value)
