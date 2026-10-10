from enum import StrEnum


class ExperimentNodeTypeName(StrEnum):
    EXPERIMENTBRANCHNODE = "ExperimentBranchNode"

    def __str__(self) -> str:
        return str(self.value)
