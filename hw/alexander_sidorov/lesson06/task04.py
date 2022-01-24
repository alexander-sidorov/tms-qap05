from datetime import date
from typing import Any
from typing import TypeVar
from typing import Union

from .common import Errors
from .common import api
from .common import typecheck

T1 = TypeVar("T1")


@api
@typecheck
def task_04(birthdays: dict[T1, date]) -> Union[T1, Errors]:
    """
    Returns the ID of the oldest person.
    """

    validate(birthdays)

    data = min(birthdays, key=lambda n: birthdays[n])

    return data


def validate(birthdays: Any) -> None:
    assert birthdays, "empty birthdays"
