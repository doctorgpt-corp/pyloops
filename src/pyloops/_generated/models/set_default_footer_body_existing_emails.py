from enum import StrEnum


class SetDefaultFooterBodyExistingEmails(StrEnum):
    ALL = "all"
    NONE = "none"
    PREVIOUSDEFAULT = "previousDefault"

    def __str__(self) -> str:
        return str(self.value)
