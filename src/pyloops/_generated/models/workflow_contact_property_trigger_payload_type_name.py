from enum import StrEnum


class WorkflowContactPropertyTriggerPayloadTypeName(StrEnum):
    CONTACTPROPERTYTRIGGER = "ContactPropertyTrigger"

    def __str__(self) -> str:
        return str(self.value)
