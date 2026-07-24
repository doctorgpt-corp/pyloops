from enum import Enum


class SendEmailActionWorkflowMutationNodeTypeName(str, Enum):
    SENDEMAILACTION = "SendEmailAction"

    def __str__(self) -> str:
        return str(self.value)
