from enum import StrEnum


class FooterWithVariantsPlacement(StrEnum):
    BELOW = "below"
    INSIDE = "inside"

    def __str__(self) -> str:
        return str(self.value)
