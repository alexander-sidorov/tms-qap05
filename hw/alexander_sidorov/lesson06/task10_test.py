from .common import validate
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
            "type(keys)=<class 'NoneType'>, MUST be a sequence",
        ],
    )
    validate(
        task_10,
        "ab",
        None,
        expected_errors=[
            "type(values)=<class 'NoneType'>, MUST be a sequence",
        ],
    )
    validate(
        task_10,
        None,
        None,
        expected_errors=[
            "type(keys)=<class 'NoneType'>, MUST be a sequence",
            "type(values)=<class 'NoneType'>, MUST be a sequence",
        ],
    )
    validate(
        task_10,
        [{}, []],
        "ab",
        expected_errors=[
            "keys[0]={} is not hashable",
            "keys[1]=[] is not hashable",
        ],
    )