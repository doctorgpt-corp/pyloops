from enum import StrEnum


class SignupTriggerTypeName(StrEnum):
    SIGNUPTRIGGER = "SignupTrigger"

    def __str__(self) -> str:
        return str(self.value)
