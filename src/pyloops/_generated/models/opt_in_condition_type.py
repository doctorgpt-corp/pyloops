from enum import StrEnum


class OptInConditionType(StrEnum):
    OPTIN = "optIn"

    def __str__(self) -> str:
        return str(self.value)
