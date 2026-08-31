from enum import StrEnum


class PropertyConditionOperator(StrEnum):
    AFTER = "after"
    ANY = "any"
    BEFORE = "before"
    BETWEEN = "between"
    CONTAINS = "contains"
    DATEEMPTY = "dateEmpty"
    DATENOTEMPTY = "dateNotEmpty"
    EMPTY = "empty"
    EQUALS = "equals"
    GREATERTHAN = "greaterThan"
    ISFALSE = "isFalse"
    ISTRUE = "isTrue"
    LESSTHAN = "lessThan"
    NOTCONTAINS = "notContains"
    NOTEMPTY = "notEmpty"
    NOTEQUALS = "notEquals"

    def __str__(self) -> str:
        return str(self.value)
