from typing import Any

import pytest

from hw._qa.hw06.common import validate_data
from hw._qa.hw06.common import validate_errors
from hw.alexander_sidorov.lesson06.task09 import task_09 as alexander_sidorov
from hw.andrey_yelin.lesson06.functions_lesson06hw import (
    reversed_dictionary_9 as andrey_yelin,
)

from .common import qual_name
from .datasets.task_09 import happy_data
from .datasets.task_09 import unhappy_data

solutions = [
    pytest.param(solution, id=qual_name(solution))
    for solution in {  # pylint: disable=use-sequence-for-iteration
        alexander_sidorov,
        andrey_yelin,
    }
]


@pytest.mark.parametrize("arg,expected", happy_data)
@pytest.mark.parametrize("solution", solutions)
def test_task_09_happy(solution: Any, arg: Any, expected: Any) -> None:
    result = solution(arg)
    validate_data(result)

    data = result["data"]
    assert data == expected


@pytest.mark.parametrize("arg", unhappy_data)
@pytest.mark.parametrize("solution", solutions)
def test_task_09_unhappy(solution: Any, arg: Any) -> None:
    result = solution(arg)
    validate_errors(result)
