from enum import StrEnum


class SimplifiedWorkflowStatus(StrEnum):
    DRAFT = "Draft"
    PAUSED = "Paused"
    PAUSEDANDQUEUEING = "PausedAndQueueing"
    SENDING = "Sending"

    def __str__(self) -> str:
        return str(self.value)
