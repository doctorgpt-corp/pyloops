from enum import StrEnum


class SignupTriggerWorkflowMutationNodeTypeName(StrEnum):
    SIGNUPTRIGGER = "SignupTrigger"

    def __str__(self) -> str:
        return str(self.value)
