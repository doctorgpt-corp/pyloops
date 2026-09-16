from enum import StrEnum


class WebhookEmailMetricPayloadSourceType(StrEnum):
    CAMPAIGN = "campaign"
    LOOP = "loop"
    TRANSACTIONAL = "transactional"

    def __str__(self) -> str:
        return str(self.value)
