from enum import StrEnum


class EmailMessageResponseWarningsItemSeverity(StrEnum):
    WARNING = "warning"

    def __str__(self) -> str:
        return str(self.value)
