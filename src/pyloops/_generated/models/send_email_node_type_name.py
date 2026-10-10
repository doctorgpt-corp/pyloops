from enum import StrEnum


class SendEmailNodeTypeName(StrEnum):
    SENDEMAILACTION = "SendEmailAction"

    def __str__(self) -> str:
        return str(self.value)
