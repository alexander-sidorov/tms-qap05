from hw.alexander_sidorov.common import validate

from .task10 import task_10


def test_task_10() -> None:
    validate(
        task_10,
        (),
        [],
        expected_data={},
    )
    validate(
        task_10,
        [1, 2, 3],
        (1, 2, 3),
        expected_data={1: 1, 2: 2, 3: 3},
    )
    validate(
        task_10,
        "ab",
        [[], [[]]],
        expected_data={"a": [], "b": [[]]},
    )
    validate(
        task_10,
        "ab",
        "a",
        expected_data={"a": "a", "b": None},
    )
    validate(
        task_10,
        "a",
        "ab",
        expected_data={"a": "a", ...: ["b"]},
    )
    validate(
        task_10,
        [None, None],
        "ab",
        expected_data={None: "b"},
    )

    validate(
        task_10,
        None,
        "ab",
        expected_errors=[
            "keys=None, NoneType != Sequence (expected)",
        ],
    )
    validate(
        task_10,
        "ab",
        None,
        expected_errors=[
            "values=None, NoneType != Sequence (expected)",
        ],
    )
    validate(
        task_10,
        [{}, None],
        "ab",
        expected_errors=[
            "keys[0]={} is not hashable",
        ],
    )
    validate(
        task_10,
        [None, []],
        "ab",
        expected_errors=[
            "keys[1]=[] is not hashable",
        ],
    )
