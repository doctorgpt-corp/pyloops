from enum import StrEnum


class WorkflowQueuedContactPolicy(StrEnum):
    DISCARD = "discard"
    FAIL = "fail"

    def __str__(self) -> str:
        return str(self.value)
