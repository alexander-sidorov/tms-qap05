from datetime import date
from typing import Any
from typing import Dict
from typing import TypeVar
from typing import Union

from .common import Errors
from .common import Result
from .common import Undefined
from .common import UndefinedType
from .common import build_result

T1 = TypeVar("T1")


def task_04(birthdays: Dict[T1, date]) -> Result:
    """
    Returns the ID of the oldest person
    """

    errors: Errors = []
    if not birthdays:
        return build_result(errors=["empty birthdays"])

    data: Any = Undefined
    min_name: Union[T1, UndefinedType] = Undefined
    min_birthday: Union[date, UndefinedType] = Undefined

    for name, birthday in birthdays.items():
        if not isinstance(birthday, date):
            errors.append(f"birthdays[{name!r}]={birthday!r}, MUST be a date")

        if errors:
            continue

        if min_name is Undefined or min_birthday > birthday:  # type: ignore
            min_name, min_birthday = name, birthday

    if not errors:
        data = min_name

    result = build_result(
        data=data,
        errors=errors,
    )

    return result
