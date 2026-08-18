from enum import Enum


class WebhookEmailMetricPayloadSourceType(str, Enum):
    CAMPAIGN = "campaign"
    LOOP = "loop"
    TRANSACTIONAL = "transactional"

    def __str__(self) -> str:
        return str(self.value)
