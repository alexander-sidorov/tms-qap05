from .common import validate
from .task08 import task_08


def test_task_08() -> None:
    validate(
        task_08,
        "",
        expected_data="",
    )
    validate(
        task_08,
        "x",
        expected_data="x1",
    )
    validate(
        task_08,
        "xxxxxxxxxxxy",
        expected_data="x11y1",
    )
    validate(
        task_08,
        "aba",
        expected_data="a1b1a1",
    )

    validate(
        task_08,
        1,
        expected_errors=[
            "flatten_text=1, int != expected: str",
        ],
    )
    validate(
        task_08,
        "aba1",
        expected_errors=[
            "integers MUST not be present in flatten text",
        ],
    )
