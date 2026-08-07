from enum import Enum


class WebhookMarketingEmailMetricPayloadSourceType(str, Enum):
    CAMPAIGN = "campaign"
    LOOP = "loop"

    def __str__(self) -> str:
        return str(self.value)
