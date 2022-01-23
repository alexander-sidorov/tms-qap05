from .common import AnySet
from .common import validate
from .task11 import task_11


def test_task_11() -> None:
    empty: AnySet = frozenset()

    validate(
        task_11,
        set(),
        empty,
        expected_data={
            "a&b": empty,
            "a|b": empty,
            "a-b": empty,
            "b-a": empty,
            "|a-b|": empty,
            "a in b": True,
            "b in a": True,
        },
    )

    validate(
        task_11,
        {1, 2, 3},
        {2, 3, 4},
        expected_data={
            "a&b": {2, 3},
            "a|b": {1, 2, 3, 4},
            "a-b": {1},
            "b-a": {4},
            "|a-b|": {1, 4},
            "a in b": False,
            "b in a": False,
        },
    )

    validate(
        task_11,
        {1, 2},
        {1, 2, 3},
        expected_data={
            "a&b": {1, 2},
            "a|b": {1, 2, 3},
            "a-b": empty,
            "b-a": {3},
            "|a-b|": {3},
            "a in b": True,
            "b in a": False,
        },
    )

    validate(
        task_11,
        {1, 2, 3},
        {1, 2},
        expected_data={
            "a&b": {1, 2},
            "a|b": {1, 2, 3},
            "a-b": {3},
            "b-a": empty,
            "|a-b|": {3},
            "a in b": False,
            "b in a": True,
        },
    )

    validate(
        task_11,
        None,
        {"ab"},
        expected_errors={
            "arg1=None, NoneType != expected: Union[frozenset, set]",
        },
    )
    validate(
        task_11,
        {"ab"},
        None,
        expected_errors={
            "arg2=None, NoneType != expected: Union[frozenset, set]",
        },
    )
