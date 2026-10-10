from enum import StrEnum


class BranchNodeTypeName(StrEnum):
    BRANCHNODE = "BranchNode"

    def __str__(self) -> str:
        return str(self.value)
