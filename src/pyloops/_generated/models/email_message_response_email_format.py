from enum import StrEnum


class EmailMessageResponseEmailFormat(StrEnum):
    PLAIN = "plain"
    STYLED = "styled"

    def __str__(self) -> str:
        return str(self.value)
