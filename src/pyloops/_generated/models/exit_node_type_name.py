from enum import StrEnum


class ExitNodeTypeName(StrEnum):
    EXITACTION = "ExitAction"

    def __str__(self) -> str:
        return str(self.value)
