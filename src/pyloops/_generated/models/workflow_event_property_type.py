from enum import StrEnum


class WorkflowEventPropertyType(StrEnum):
    BOOLEAN = "boolean"
    DATE = "date"
    NUMBER = "number"
    STRING = "string"

    def __str__(self) -> str:
        return str(self.value)
