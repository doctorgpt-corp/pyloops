from enum import StrEnum


class SimplifiedContactPropertyTriggerWorkflowNodeTypeName(StrEnum):
    CONTACTPROPERTYTRIGGER = "ContactPropertyTrigger"

    def __str__(self) -> str:
        return str(self.value)
