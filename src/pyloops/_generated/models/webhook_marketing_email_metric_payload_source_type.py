from enum import StrEnum


class WebhookMarketingEmailMetricPayloadSourceType(StrEnum):
    CAMPAIGN = "campaign"
    LOOP = "loop"

    def __str__(self) -> str:
        return str(self.value)
