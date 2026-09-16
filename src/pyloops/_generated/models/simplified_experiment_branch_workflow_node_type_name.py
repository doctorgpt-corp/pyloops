from enum import StrEnum


class SimplifiedExperimentBranchWorkflowNodeTypeName(StrEnum):
    EXPERIMENTBRANCHNODE = "ExperimentBranchNode"

    def __str__(self) -> str:
        return str(self.value)
