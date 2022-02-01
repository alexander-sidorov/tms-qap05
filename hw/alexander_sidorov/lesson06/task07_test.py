from hw.alexander_sidorov.common import validate

from .task07 import task_07


def test_task_07() -> None:
    validate(
        task_07,
        "",
        expected_data="",
    )
    validate(
        task_07,
        "x0",
        expected_data="",
    )
    validate(
        task_07,
        "x1",
        expected_data="x",
    )
    validate(
        task_07,
        "x11",
        expected_data="x" * 11,
    )
    validate(
        task_07,
        "x11y12",
        expected_data="x" * 11 + "y" * 12,
    )

    validate(
        task_07,
        1,
        expected_errors=[
            "folded_text=1, int != str (expected)",
        ],
    )
    validate(
        task_07,
        "xx11y12",
        expected_errors=[
            "folded_text='xx11y12' is malformed",
        ],
    )
