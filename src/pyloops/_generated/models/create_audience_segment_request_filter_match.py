from enum import StrEnum


class CreateAudienceSegmentRequestFilterMatch(StrEnum):
    ALL = "all"
    ANY = "any"

    def __str__(self) -> str:
        return str(self.value)
