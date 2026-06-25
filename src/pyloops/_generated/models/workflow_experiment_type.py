from enum import Enum


class WorkflowExperimentType(str, Enum):
    AUTOSPLIT = "autosplit"
    WEBHOOK = "webhook"

    def __str__(self) -> str:
        return str(self.value)
