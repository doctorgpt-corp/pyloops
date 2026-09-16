from enum import StrEnum


class WorkflowQueuedContactDeletePreviewStatus(StrEnum):
    DRYRUN = "dryRun"
    QUEUEDCONTACTSFOUND = "queuedContactsFound"

    def __str__(self) -> str:
        return str(self.value)
