from enum import StrEnum


class VariantWorkflowNodeTypeName(StrEnum):
    VARIANTNODE = "VariantNode"

    def __str__(self) -> str:
        return str(self.value)
