from enum import StrEnum


class EventPatternIncomingWebhookPlatform(StrEnum):
    CLERK = "clerk"
    NULL = "null"
    POLAR = "polar"
    STRIPE = "stripe"
    SUPABASE = "supabase"

    def __str__(self) -> str:
        return str(self.value)
