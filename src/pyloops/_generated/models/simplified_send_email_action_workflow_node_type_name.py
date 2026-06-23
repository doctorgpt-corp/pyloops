from enum import Enum


class SimplifiedSendEmailActionWorkflowNodeTypeName(str, Enum):
    SENDEMAILACTION = "SendEmailAction"

    def __str__(self) -> str:
        return str(self.value)
