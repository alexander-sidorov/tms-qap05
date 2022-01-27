from typing import Any

import pytest

from hw._qa.hw06.common import validate_data
from hw._qa.hw06.common import validate_errors
from hw.alexander_sidorov.lesson06.task07 import task_07 as alexander_sidorov
from hw.yaroslav_belaychuk.lesson006HW import zadacha_7 as yaroslav_belaychuk

from .common import qual_name
from .datasets.task_07 import happy_data
from .datasets.task_07 import unhappy_data

solutions = [
    pytest.param(solution, id=qual_name(solution))
    for solution in {  # pylint: disable=use-sequence-for-iteration
        alexander_sidorov,
        yaroslav_belaychuk,
    }
]


@pytest.mark.parametrize("arg,expected", happy_data)
@pytest.mark.parametrize("solution", solutions)
def test_task_07_happy(solution: Any, arg: Any, expected: Any) -> None:
    result = solution(arg)
    validate_data(result)

    data = result["data"]
    assert data == expected


@pytest.mark.parametrize("arg", unhappy_data)
@pytest.mark.parametrize("solution", solutions)
def test_task_07_unhappy(solution: Any, arg: Any) -> None:
    result = solution(arg)
    validate_errors(result)
