from typing import Any

import pytest

from hw._qa.hw06.common import validate_data
from hw._qa.hw06.common import validate_errors
from hw.alexander_sidorov.lesson06.task10 import task_10 as alexander_sidorov
from hw.vadim_maletski.func6 import level_10 as vadim_maletski

from .common import qual_name
from .datasets.task_10 import happy_data
from .datasets.task_10 import unhappy_data

solutions = [
    pytest.param(solution, id=qual_name(solution))
    for solution in {  # pylint: disable=use-sequence-for-iteration
        alexander_sidorov,
        vadim_maletski,
    }
]


@pytest.mark.parametrize("arg1,arg2,expected", happy_data)
@pytest.mark.parametrize("solution", solutions)
def test_task_10_happy(
    solution: Any, arg1: Any, arg2: Any, expected: Any
) -> None:
    result = solution(arg1, arg2)
    validate_data(result)

    data = result["data"]
    assert data == expected


@pytest.mark.parametrize("arg1,arg2", unhappy_data)
@pytest.mark.parametrize("solution", solutions)
def test_task_10_unhappy(solution: Any, arg1: Any, arg2: Any) -> None:
    result = solution(arg1, arg2)
    validate_errors(result)
