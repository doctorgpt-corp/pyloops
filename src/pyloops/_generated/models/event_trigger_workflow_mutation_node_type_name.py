from enum import StrEnum


class EventTriggerWorkflowMutationNodeTypeName(StrEnum):
    EVENTTRIGGER = "EventTrigger"

    def __str__(self) -> str:
        return str(self.value)
