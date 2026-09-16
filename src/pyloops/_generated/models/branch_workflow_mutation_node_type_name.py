from enum import StrEnum


class BranchWorkflowMutationNodeTypeName(StrEnum):
    BRANCHNODE = "BranchNode"

    def __str__(self) -> str:
        return str(self.value)
