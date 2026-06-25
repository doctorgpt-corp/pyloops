from enum import Enum


class EmailMessageResponseWarningsItemSeverity(str, Enum):
    WARNING = "warning"

    def __str__(self) -> str:
        return str(self.value)
