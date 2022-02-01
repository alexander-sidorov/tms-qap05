from .common import validate
from .task02 import task_02


def test_task_02() -> None:
    validate(task_02, "a", 2, expected_data="aa")
    validate(task_02, (3,), 2, expected_data=(3, 3))
    validate(task_02, 0.2, 5, expected_data=1.0)
    validate(task_02, 1j, -1j, expected_data=1)
    validate(task_02, 1, 2, 3, expected_data=6)
    validate(task_02, 1, 2, expected_data=2)
    validate(task_02, 1, expected_data=1)
    validate(task_02, 2, "b", expected_data="bb")
    validate(task_02, 2, "c", 3, expected_data="cccccc")
    validate(task_02, [2], 2, expected_data=[2, 2])
    validate(task_02, True, False, expected_data=0)

    validate(
        task_02,
        None,
        2,
        expected_errors={
            "*args[0]=None, NoneType != expected: Union[Number, Sequence]",
        },
    )
    validate(
        task_02,
        {},
        2,
        expected_errors={
            "*args[0]={}, dict != expected: Union[Number, Sequence]",
        },
    )
    validate(
        task_02,
        2,
        "c",
        3,
        "c",
        expected_errors={
            "cannot multiply 2 sequences",
        },
    )
    validate(
        task_02,
        2,
        "c",
        3j,
        expected_errors={
            "cannot multiply sequences and non-ints",
        },
    )
    validate(
        task_02,
        expected_errors={
            "nothing to multiply",
        },
    )
