from enum import Enum


class WorkflowSignupTriggerPayloadTypeName(str, Enum):
    SIGNUPTRIGGER = "SignupTrigger"

    def __str__(self) -> str:
        return str(self.value)
