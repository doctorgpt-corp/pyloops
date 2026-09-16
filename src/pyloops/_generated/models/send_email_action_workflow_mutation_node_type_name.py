from enum import StrEnum


class SendEmailActionWorkflowMutationNodeTypeName(StrEnum):
    SENDEMAILACTION = "SendEmailAction"

    def __str__(self) -> str:
        return str(self.value)
