from enum import Enum


class ContactPropertyTriggerWorkflowNodeTypeName(str, Enum):
    CONTACTPROPERTYTRIGGER = "ContactPropertyTrigger"

    def __str__(self) -> str:
        return str(self.value)
