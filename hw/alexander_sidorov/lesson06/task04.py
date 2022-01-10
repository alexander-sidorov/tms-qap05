from datetime import date
from typing import Dict
from typing import TypeVar

from .common import Result

T1 = TypeVar("T1")


def task_04(birthdays: Dict[T1, date]) -> Result:
    """
    Returns the ID of the oldest person
    """

    name: T1
    _birthday: date
    name, _birthday = min(
        birthdays.items(),
        key=lambda _pair: _pair[1],
    )

    return {"data": name}
