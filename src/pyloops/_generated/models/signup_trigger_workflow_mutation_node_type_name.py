from enum import Enum


class SignupTriggerWorkflowMutationNodeTypeName(str, Enum):
    SIGNUPTRIGGER = "SignupTrigger"

    def __str__(self) -> str:
        return str(self.value)
