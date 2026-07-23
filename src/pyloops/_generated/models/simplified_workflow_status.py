from enum import Enum


class SimplifiedWorkflowStatus(str, Enum):
    DRAFT = "Draft"
    PAUSED = "Paused"
    PAUSEDANDQUEUEING = "PausedAndQueueing"
    SENDING = "Sending"

    def __str__(self) -> str:
        return str(self.value)
