from enum import StrEnum


class SimplifiedBranchWorkflowNodeTypeName(StrEnum):
    BRANCHNODE = "BranchNode"

    def __str__(self) -> str:
        return str(self.value)
