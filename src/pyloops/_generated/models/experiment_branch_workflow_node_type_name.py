from enum import StrEnum


class ExperimentBranchWorkflowNodeTypeName(StrEnum):
    EXPERIMENTBRANCHNODE = "ExperimentBranchNode"

    def __str__(self) -> str:
        return str(self.value)
