from enum import StrEnum


class MailingListOptInType(StrEnum):
    OPTIN = "optIn"

    def __str__(self) -> str:
        return str(self.value)
