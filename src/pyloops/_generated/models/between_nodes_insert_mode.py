from enum import StrEnum


class BetweenNodesInsertMode(StrEnum):
    BETWEEN = "between"

    def __str__(self) -> str:
        return str(self.value)
