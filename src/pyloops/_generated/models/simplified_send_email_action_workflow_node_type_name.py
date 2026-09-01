from enum import StrEnum


class SimplifiedSendEmailActionWorkflowNodeTypeName(StrEnum):
    SENDEMAILACTION = "SendEmailAction"

    def __str__(self) -> str:
        return str(self.value)
