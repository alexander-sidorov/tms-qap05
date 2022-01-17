from datetime import date
from typing import Any
from typing import Optional
from typing import TypeVar
from typing import Union

from .common import Errors
from .common import ErrorsList
from .common import api

T1 = TypeVar("T1")


@api
def task_04(birthdays: dict[T1, date]) -> Union[T1, Errors]:
    """
    Returns the ID of the oldest person.
    """

    if errors := validate(birthdays):
        return errors

    data = min(birthdays, key=lambda n: birthdays[n])

    return data


def validate(birthdays: Any) -> Optional[Errors]:
    errors: ErrorsList = []

    if not birthdays:
        errors.append("empty birthdays")

    if not isinstance(birthdays, dict):
        errors.append(f"{type(birthdays)=}, MUST be a dict")
    else:
        for name, birthday in birthdays.items():
            if not isinstance(birthday, date):
                errors.append(
                    f"birthdays[{name!r}]={birthday!r}, MUST be a date"
                )

    return {"errors": sorted(errors)} if errors else None
