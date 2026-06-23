from enum import Enum


class PropertyConditionType(str, Enum):
    PROPERTY = "property"

    def __str__(self) -> str:
        return str(self.value)
