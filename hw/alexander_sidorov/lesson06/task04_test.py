from datetime import date

from .common import validate
from .task04 import task_04


def test_task_04() -> None:
    validate(
        task_04,
        {
            1: date(year=1987, month=8, day=2),
            (): date(year=1987, month=8, day=1),
            ...: date(year=1987, month=7, day=1),
            "a": date(year=1987, month=8, day=3),
        },
        expected_data=...,
    )

    validate(
        task_04,
        {1, 2, 3},
        expected_errors=[
            "type(birthdays)=<class 'set'>, MUST be a dict",
        ],
    )

    validate(
        task_04,
        {
            1: date(year=1987, month=8, day=2),
            (): None,
            ...: ...,
        },
        expected_errors=[
            "birthdays[()]=None, MUST be a date",
            "birthdays[Ellipsis]=Ellipsis, MUST be a date",
        ],
    )

    validate(
        task_04,
        {},
        expected_errors=[
            "empty birthdays",
        ],
    )
