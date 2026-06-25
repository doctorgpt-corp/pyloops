from enum import Enum


class SimplifiedSignupTriggerWorkflowNodeTypeName(str, Enum):
    SIGNUPTRIGGER = "SignupTrigger"

    def __str__(self) -> str:
        return str(self.value)
