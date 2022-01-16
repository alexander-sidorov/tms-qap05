from datetime import date
from typing import Any
from typing import Dict
from typing import TypeVar

from .common import Errors
from .common import Undefined
from .common import api
from .common import build_result

T1 = TypeVar("T1")


@api
def task_04(birthdays: Dict[T1, date]) -> Any:
    """
    Returns the ID of the oldest person
    """

    errors: Errors = []
    if not birthdays:
        return build_result(errors=["empty birthdays"])

    for name, birthday in birthdays.items():
        if not isinstance(birthday, date):
            errors.append(f"birthdays[{name!r}]={birthday!r}, MUST be a date")

    data = (
        min(birthdays, key=lambda n: birthdays[n]) if not errors else Undefined
    )

    if data is not Undefined:
        return data

    return build_result(errors=errors)
