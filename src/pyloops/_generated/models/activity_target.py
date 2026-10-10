from enum import StrEnum


class ActivityTarget(StrEnum):
    CAMPAIGN = "campaign"
    WORKFLOW = "workflow"
    WORKFLOWEMAIL = "workflowEmail"

    def __str__(self) -> str:
        return str(self.value)
