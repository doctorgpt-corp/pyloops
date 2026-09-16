from enum import StrEnum


class UpdateEmailMessageRequestEmailFormat(StrEnum):
    PLAIN = "plain"
    STYLED = "styled"

    def __str__(self) -> str:
        return str(self.value)
