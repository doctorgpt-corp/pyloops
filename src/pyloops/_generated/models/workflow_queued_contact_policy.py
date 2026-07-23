from enum import Enum


class WorkflowQueuedContactPolicy(str, Enum):
    DISCARD = "discard"
    FAIL = "fail"

    def __str__(self) -> str:
        return str(self.value)
