from typing import Any

import pytest

from hw._qa.hw06.common import validate_data
from hw._qa.hw06.common import validate_errors
from hw.alexander_sidorov.lesson06.task12 import task_12 as alexander_sidorov

from .common import qual_name
from .datasets.task_12 import happy_data
from .datasets.task_12 import unhappy_data

solutions = [
    pytest.param(solution, id=qual_name(solution))
    for solution in {  # pylint: disable=use-sequence-for-iteration
        alexander_sidorov,
    }
]


@pytest.mark.parametrize("args,expected", happy_data)
@pytest.mark.parametrize("solution", solutions)
def test_task_12_happy(solution: Any, args: Any, expected: Any) -> None:
    result = solution(*args)
    validate_data(result)

    data = result["data"]
    assert data == expected


@pytest.mark.parametrize("args", unhappy_data)
@pytest.mark.parametrize("solution", solutions)
def test_task_12_unhappy(solution: Any, args: Any) -> None:
    result = solution(*args)
    validate_errors(result)
