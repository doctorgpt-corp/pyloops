from enum import StrEnum


class MailingListUpdatedStatus(StrEnum):
    UPDATED = "updated"

    def __str__(self) -> str:
        return str(self.value)
