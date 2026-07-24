from enum import Enum


class AddToListTriggerWorkflowMutationNodeTypeName(str, Enum):
    ADDTOLISTTRIGGER = "AddToListTrigger"

    def __str__(self) -> str:
        return str(self.value)
