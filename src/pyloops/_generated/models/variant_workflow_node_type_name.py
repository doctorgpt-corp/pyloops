from enum import Enum


class VariantWorkflowNodeTypeName(str, Enum):
    VARIANTNODE = "VariantNode"

    def __str__(self) -> str:
        return str(self.value)
