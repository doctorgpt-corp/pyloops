from enum import Enum


class ContactPropertyTriggerWorkflowMutationNodeTypeName(str, Enum):
    CONTACTPROPERTYTRIGGER = "ContactPropertyTrigger"

    def __str__(self) -> str:
        return str(self.value)
