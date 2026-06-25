from enum import Enum


class ExperimentBranchWorkflowNodeTypeName(str, Enum):
    EXPERIMENTBRANCHNODE = "ExperimentBranchNode"

    def __str__(self) -> str:
        return str(self.value)
