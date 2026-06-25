from enum import Enum


class EmailMessageResponseEmailFormat(str, Enum):
    PLAIN = "plain"
    STYLED = "styled"

    def __str__(self) -> str:
        return str(self.value)
