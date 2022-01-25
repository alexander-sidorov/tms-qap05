from .common import validate
from .task01 import task_01


def test_task_01() -> None:
    validate(task_01, "", expected_data=True)
    validate(task_01, "x", expected_data=True)
    validate(task_01, "xx", expected_data=True)
    validate(task_01, "xy", expected_data=False)

    validate(
        task_01,
        None,
        expected_errors=[
            "arg=None, NoneType != str (expected)",
        ],
    )
    validate(
        task_01,
        1,
        expected_errors=[
            "arg=1, int != str (expected)",
        ],
    )
