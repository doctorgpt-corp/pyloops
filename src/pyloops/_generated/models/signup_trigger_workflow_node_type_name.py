from enum import StrEnum


class SignupTriggerWorkflowNodeTypeName(StrEnum):
    SIGNUPTRIGGER = "SignupTrigger"

    def __str__(self) -> str:
        return str(self.value)
