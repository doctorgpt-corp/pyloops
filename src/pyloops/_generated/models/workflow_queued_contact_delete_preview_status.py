from enum import Enum


class WorkflowQueuedContactDeletePreviewStatus(str, Enum):
    DRYRUN = "dryRun"
    QUEUEDCONTACTSFOUND = "queuedContactsFound"

    def __str__(self) -> str:
        return str(self.value)
