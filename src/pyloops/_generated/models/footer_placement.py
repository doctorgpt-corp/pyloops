from enum import StrEnum


class FooterPlacement(StrEnum):
    BELOW = "below"
    INSIDE = "inside"

    def __str__(self) -> str:
        return str(self.value)
