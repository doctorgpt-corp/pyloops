from enum import Enum


class SimplifiedVariantWorkflowNodeTypeName(str, Enum):
    VARIANTNODE = "VariantNode"

    def __str__(self) -> str:
        return str(self.value)
