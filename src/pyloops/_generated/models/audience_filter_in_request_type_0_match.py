from enum import StrEnum


class AudienceFilterInRequestType0Match(StrEnum):
    ALL = "all"
    ANY = "any"

    def __str__(self) -> str:
        return str(self.value)
