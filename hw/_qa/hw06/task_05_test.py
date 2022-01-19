from typing import Any

import pytest

from hw._qa.hw06.common import validate_data
from hw._qa.hw06.common import validate_errors
from hw.alexander_sidorov.lesson06.task05 import task_05 as alexander_sidorov
from hw.siarhei_apanel.refakt import repeat as siarhei_apanel

from .common import qual_name
from .datasets.task_05 import happy_data
from .datasets.task_05 import unhappy_data

solutions = [
    pytest.param(solution, id=qual_name(solution))
    for solution in {
        alexander_sidorov,
        siarhei_apanel,
    }
]


@pytest.mark.parametrize("arg,expected", happy_data)
@pytest.mark.parametrize("solution", solutions)
def test_task_05_happy(solution: Any, arg: Any, expected: Any) -> None:
    result = solution(arg)
    validate_data(result)

    data = result["data"]
    assert data == expected


@pytest.mark.parametrize("arg", unhappy_data)
@pytest.mark.parametrize("solution", solutions)
def test_task_05_unhappy(solution: Any, arg: Any) -> None:
    result = solution(arg)
    validate_errors(result)
