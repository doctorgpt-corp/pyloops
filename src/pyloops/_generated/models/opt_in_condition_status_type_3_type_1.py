from enum import StrEnum


class OptInConditionStatusType3Type1(StrEnum):
    ACCEPTED = "accepted"
    PENDING = "pending"
    REJECTED = "rejected"

    def __str__(self) -> str:
        return str(self.value)
