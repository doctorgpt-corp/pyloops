from enum import Enum


class WorkflowContactPropertyTriggerPayloadTypeName(str, Enum):
    CONTACTPROPERTYTRIGGER = "ContactPropertyTrigger"

    def __str__(self) -> str:
        return str(self.value)
