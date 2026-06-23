from enum import Enum


class WorkflowContactPropertyComparisonOperator(str, Enum):
    ACCEPTED_OPT_IN = "accepted_opt_in"
    AFTER = "after"
    ANY = "any"
    ANY_LOOP_EMAIL = "any_loop_email"
    BEFORE = "before"
    BETWEEN = "between"
    CAMPAIGN = "campaign"
    CONTAINS = "contains"
    DATE_EMPTY = "date_empty"
    DATE_NOT_EMPTY = "date_not_empty"
    EMPTY = "empty"
    EQUAL = "equal"
    FALSE = "false"
    GREATER_THAN = "greater_than"
    LESS_THAN = "less_than"
    NOT_CONTAINS = "not_contains"
    NOT_EMPTY = "not_empty"
    NOT_EQUAL = "not_equal"
    NOT_OPT_IN = "not_opt_in"
    NUMERIC_EQUAL = "numeric_equal"
    NUMERIC_NOT_EQUAL = "numeric_not_equal"
    PENDING_OPT_IN = "pending_opt_in"
    REJECTED_OPT_IN = "rejected_opt_in"
    SPECIFIC_LOOP_EMAIL = "specific_loop_email"
    TRUE = "true"

    def __str__(self) -> str:
        return str(self.value)
