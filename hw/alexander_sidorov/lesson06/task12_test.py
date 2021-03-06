from typing import Any

from hw.alexander_sidorov.common import validate

from .task12 import task_12


def test_task_12() -> None:
    args: Any

    args = (1, 2)
    validate(
        task_12,
        *args,
        expected_data={1: 2},
    )

    args = "ab"
    validate(
        task_12,
        *args,
        expected_data={"a": "b"},
    )

    args = (None, [], ..., {})
    validate(
        task_12,
        *args,
        expected_data={None: [], ...: {}},
    )

    args = "a" * 20
    validate(
        task_12,
        *args,
        expected_data={"a": "a"},
    )

    args = "a" * 19
    validate(
        task_12,
        *args,
        expected_errors=["odd number of elements (19)"],
    )

    args = [[], None]
    validate(
        task_12,
        *args,
        expected_errors={
            "args[0]=[] is not hashable",
        },
    )
