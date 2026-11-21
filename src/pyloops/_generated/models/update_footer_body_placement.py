from enum import StrEnum


class UpdateFooterBodyPlacement(StrEnum):
    BELOW = "below"
    INSIDE = "inside"

    def __str__(self) -> str:
        return str(self.value)
