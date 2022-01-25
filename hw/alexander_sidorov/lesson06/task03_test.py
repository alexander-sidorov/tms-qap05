from datetime import date

from .common import validate
from .task03 import task_03


def test_task_03() -> None:
    today = date.today()

    ymd = (today.year - 10, today.month, today.day)

    validate(
        task_03,
        date(*ymd),
        expected_data={
            "year": ymd[0],
            "month": ymd[1],
            "day": ymd[2],
            "age": 10,
        },
    )

    validate(
        task_03,
        None,
        expected_errors=[
            "arg=None, NoneType != date (expected)",
        ],
    )
