from enum import Enum


class SignupTriggerWorkflowNodeTypeName(str, Enum):
    SIGNUPTRIGGER = "SignupTrigger"

    def __str__(self) -> str:
        return str(self.value)
