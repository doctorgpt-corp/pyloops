from enum import StrEnum


class CreateWorkflowNodeTypeName(StrEnum):
    AUDIENCEFILTER = "AudienceFilter"
    BRANCHNODE = "BranchNode"
    EXPERIMENTBRANCHNODE = "ExperimentBranchNode"
    SENDEMAILACTION = "SendEmailAction"
    TIMERACTION = "TimerAction"
    VARIANTNODE = "VariantNode"

    def __str__(self) -> str:
        return str(self.value)
