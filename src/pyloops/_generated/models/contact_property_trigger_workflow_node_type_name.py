from enum import StrEnum


class ContactPropertyTriggerWorkflowNodeTypeName(StrEnum):
    CONTACTPROPERTYTRIGGER = "ContactPropertyTrigger"

    def __str__(self) -> str:
        return str(self.value)
