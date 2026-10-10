from enum import StrEnum


class AfterANodeInsertMode(StrEnum):
    AFTER = "after"

    def __str__(self) -> str:
        return str(self.value)
