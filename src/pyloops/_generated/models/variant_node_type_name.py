from enum import StrEnum


class VariantNodeTypeName(StrEnum):
    VARIANTNODE = "VariantNode"

    def __str__(self) -> str:
        return str(self.value)
