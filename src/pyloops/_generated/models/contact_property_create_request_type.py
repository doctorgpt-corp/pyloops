from enum import Enum


class ContactPropertyCreateRequestType(str, Enum):
    BOOLEAN = "boolean"
    DATE = "date"
    NUMBER = "number"
    STRING = "string"

    def __str__(self) -> str:
        return str(self.value)
