from enum import StrEnum


class WorkflowContactPropertyComparisonOperator(StrEnum):
    AFTER = "after"
    ANY = "any"
    BEFORE = "before"
    BETWEEN = "between"
    CONTAINS = "contains"
    EMPTY = "empty"
    EQUAL = "equal"
    FALSE = "false"
    GREATER_THAN = "greater_than"
    LESS_THAN = "less_than"
    NOT_CONTAINS = "not_contains"
    NOT_EMPTY = "not_empty"
    NOT_EQUAL = "not_equal"
    NUMERIC_EQUAL = "numeric_equal"
    NUMERIC_NOT_EQUAL = "numeric_not_equal"
    TRUE = "true"

    def __str__(self) -> str:
        return str(self.value)
