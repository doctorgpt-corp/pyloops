from enum import StrEnum


class AudienceFilterType0Match(StrEnum):
    ALL = "all"
    ANY = "any"

    def __str__(self) -> str:
        return str(self.value)
