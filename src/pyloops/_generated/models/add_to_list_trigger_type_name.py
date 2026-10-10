from enum import StrEnum


class AddToListTriggerTypeName(StrEnum):
    ADDTOLISTTRIGGER = "AddToListTrigger"

    def __str__(self) -> str:
        return str(self.value)
