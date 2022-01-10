from .common import validate
from .task06 import task_06


def test_task_06() -> None:
    validate(
        task_06,
        "",
        expected_data={},
    )
    validate(
        task_06,
        "xx=",
        expected_data={
            "xx": [""],
        },
    )
    validate(
        task_06,
        "xx=&yy=",
        expected_data={
            "xx": [""],
            "yy": [""],
        },
    )
    validate(
        task_06,
        "xx=1&yy=2",
        expected_data={
            "xx": ["1"],
            "yy": ["2"],
        },
    )
    validate(
        task_06,
        "xx=1&yy=2&&yy=3",
        expected_data={
            "xx": ["1"],
            "yy": ["2", "3"],
        },
    )

    validate(
        task_06,
        1,
        expected_errors=[
            "type(query)=<class 'int'>, MUST be a str",
        ],
    )
