from enum import Enum


class WorkflowEventTriggerPayloadTypeName(str, Enum):
    EVENTTRIGGER = "EventTrigger"

    def __str__(self) -> str:
        return str(self.value)
