from enum import StrEnum


class ContactPropertyTriggerTypeName(StrEnum):
    CONTACTPROPERTYTRIGGER = "ContactPropertyTrigger"

    def __str__(self) -> str:
        return str(self.value)
