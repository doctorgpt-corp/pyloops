from enum import Enum


class BranchWorkflowMutationNodeTypeName(str, Enum):
    BRANCHNODE = "BranchNode"

    def __str__(self) -> str:
        return str(self.value)
