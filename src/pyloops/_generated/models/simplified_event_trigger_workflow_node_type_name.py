from enum import StrEnum


class SimplifiedEventTriggerWorkflowNodeTypeName(StrEnum):
    EVENTTRIGGER = "EventTrigger"

    def __str__(self) -> str:
        return str(self.value)
