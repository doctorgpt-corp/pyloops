from enum import StrEnum


class VariantWorkflowMutationNodeTypeName(StrEnum):
    VARIANTNODE = "VariantNode"

    def __str__(self) -> str:
        return str(self.value)
