from enum import StrEnum


class ExperimentBranchWorkflowMutationNodeTypeName(StrEnum):
    EXPERIMENTBRANCHNODE = "ExperimentBranchNode"

    def __str__(self) -> str:
        return str(self.value)
