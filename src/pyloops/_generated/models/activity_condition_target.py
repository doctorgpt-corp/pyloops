from enum import Enum


class ActivityConditionTarget(str, Enum):
    CAMPAIGN = "campaign"
    WORKFLOW = "workflow"
    WORKFLOWEMAIL = "workflowEmail"

    def __str__(self) -> str:
        return str(self.value)
