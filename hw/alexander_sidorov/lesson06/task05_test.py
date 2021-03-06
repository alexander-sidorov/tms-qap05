from hw.alexander_sidorov.common import validate

from .task05 import task_05


def test_task_05() -> None:
    validate(
        task_05,
        "",
        expected_data={},
    )
    validate(
        task_05,
        "abc",
        expected_data={},
    )
    validate(
        task_05,
        "aaab",
        expected_data={"a": 3},
    )
    validate(
        task_05,
        {1, 2, 3},
        expected_data={},
    )

    validate(
        task_05,
        None,
        expected_errors={
            "collection=None, NoneType != Collection (expected)",
        },
    )

    validate(
        task_05,
        [[]],
        expected_errors={
            "collection[0]=[] is not hashable",
        },
    )
