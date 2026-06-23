from enum import Enum


class SimplifiedExperimentBranchWorkflowNodeTypeName(str, Enum):
    EXPERIMENTBRANCHNODE = "ExperimentBranchNode"

    def __str__(self) -> str:
        return str(self.value)
