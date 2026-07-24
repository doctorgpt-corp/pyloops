from enum import Enum


class ExperimentBranchWorkflowMutationNodeTypeName(str, Enum):
    EXPERIMENTBRANCHNODE = "ExperimentBranchNode"

    def __str__(self) -> str:
        return str(self.value)
