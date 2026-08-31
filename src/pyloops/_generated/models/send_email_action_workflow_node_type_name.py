from enum import StrEnum


class SendEmailActionWorkflowNodeTypeName(StrEnum):
    SENDEMAILACTION = "SendEmailAction"

    def __str__(self) -> str:
        return str(self.value)
