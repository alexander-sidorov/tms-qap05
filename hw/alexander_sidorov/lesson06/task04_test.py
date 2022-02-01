from datetime import date

from hw.alexander_sidorov.common import validate

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
            "birthdays={1, 2, 3}, set != dict (expected)",
        ],
    )

    validate(
        task_04,
        {
            1: date(year=1987, month=8, day=2),
            ...: ...,
        },
        expected_errors=[
            "birthdays[Ellipsis]=Ellipsis, ellipsis != date (expected)",
        ],
    )

    validate(
        task_04,
        {},
        expected_errors=[
            "empty birthdays",
        ],
    )
