from enum import Enum


class CreateWorkflowNodeTypeName(str, Enum):
    AUDIENCEFILTER = "AudienceFilter"
    BRANCHNODE = "BranchNode"
    EXPERIMENTBRANCHNODE = "ExperimentBranchNode"
    SENDEMAILACTION = "SendEmailAction"
    TIMERACTION = "TimerAction"
    VARIANTNODE = "VariantNode"

    def __str__(self) -> str:
        return str(self.value)
