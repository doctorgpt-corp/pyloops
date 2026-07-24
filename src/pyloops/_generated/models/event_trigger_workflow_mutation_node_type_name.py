from enum import Enum


class EventTriggerWorkflowMutationNodeTypeName(str, Enum):
    EVENTTRIGGER = "EventTrigger"

    def __str__(self) -> str:
        return str(self.value)
