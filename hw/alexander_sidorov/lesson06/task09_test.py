from hw.alexander_sidorov.common import validate

from .task09 import task_09


def test_task_09() -> None:
    validate(
        task_09,
        {},
        expected_data={},
    )
    validate(
        task_09,
        {1: 2},
        expected_data={2: 1},
    )
    validate(
        task_09,
        {1: 2, 3: 2},
        expected_data={2: [1, 3]},
    )

    validate(
        task_09,
        1,
        expected_errors=[
            "arg=1, int != dict (expected)",
        ],
    )
    validate(
        task_09,
        {1: {}},
        expected_errors=[
            "value={} of key=1 cannot be used as a new key",
        ],
    )
