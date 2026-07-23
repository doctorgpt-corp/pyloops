from enum import Enum


class VariantWorkflowMutationNodeTypeName(str, Enum):
    VARIANTNODE = "VariantNode"

    def __str__(self) -> str:
        return str(self.value)
