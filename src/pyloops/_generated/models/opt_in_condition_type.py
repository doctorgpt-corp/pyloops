from enum import Enum


class OptInConditionType(str, Enum):
    OPTIN = "optIn"

    def __str__(self) -> str:
        return str(self.value)
