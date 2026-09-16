from enum import StrEnum


class BranchWorkflowNodeTypeName(StrEnum):
    BRANCHNODE = "BranchNode"

    def __str__(self) -> str:
        return str(self.value)
