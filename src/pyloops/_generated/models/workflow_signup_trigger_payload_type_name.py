from enum import StrEnum


class WorkflowSignupTriggerPayloadTypeName(StrEnum):
    SIGNUPTRIGGER = "SignupTrigger"

    def __str__(self) -> str:
        return str(self.value)
