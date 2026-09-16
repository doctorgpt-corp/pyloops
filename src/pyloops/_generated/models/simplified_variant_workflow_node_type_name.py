from enum import StrEnum


class SimplifiedVariantWorkflowNodeTypeName(StrEnum):
    VARIANTNODE = "VariantNode"

    def __str__(self) -> str:
        return str(self.value)
