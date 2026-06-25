from enum import Enum


class SendEmailActionWorkflowNodeTypeName(str, Enum):
    SENDEMAILACTION = "SendEmailAction"

    def __str__(self) -> str:
        return str(self.value)
