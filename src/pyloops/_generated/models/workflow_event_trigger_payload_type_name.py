from enum import StrEnum


class WorkflowEventTriggerPayloadTypeName(StrEnum):
    EVENTTRIGGER = "EventTrigger"

    def __str__(self) -> str:
        return str(self.value)
