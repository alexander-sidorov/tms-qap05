from datetime import date

from freezegun import freeze_time

from .common import validate
from .task03 import task_03


@freeze_time(date(2000, 1, 1))
def test_task_03() -> None:
    validate(
        task_03,
        date(year=1987, month=8, day=2),
        expected_data={
            "year": 1987,
            "month": 8,
            "day": 2,
            "age": 12,
        },
    )

    validate(
        task_03,
        None,
        expected_errors=[
            "type(arg)=<class 'NoneType'>, MUST be a date",
        ],
    )
