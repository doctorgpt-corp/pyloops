from enum import StrEnum


class PropertyConditionType(StrEnum):
    PROPERTY = "property"

    def __str__(self) -> str:
        return str(self.value)
