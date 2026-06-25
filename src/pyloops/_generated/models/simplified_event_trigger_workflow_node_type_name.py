from enum import Enum


class SimplifiedEventTriggerWorkflowNodeTypeName(str, Enum):
    EVENTTRIGGER = "EventTrigger"

    def __str__(self) -> str:
        return str(self.value)
