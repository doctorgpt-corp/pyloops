from enum import Enum


class WorkflowMailingListPreviewStatus(str, Enum):
    DRYRUN = "dryRun"
    QUEUEDCONTACTSFOUND = "queuedContactsFound"

    def __str__(self) -> str:
        return str(self.value)
