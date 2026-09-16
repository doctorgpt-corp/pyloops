from enum import StrEnum


class SimplifiedSignupTriggerWorkflowNodeTypeName(StrEnum):
    SIGNUPTRIGGER = "SignupTrigger"

    def __str__(self) -> str:
        return str(self.value)
