from typing import Any

import pytest

from hw._qa.hw06.common import validate_data
from hw._qa.hw06.common import validate_errors
from hw.alexander_sidorov.lesson06.task11 import task_11 as alexander_sidorov
from hw.siarhei_apanel.refakt import new_set as siarhei_apanel
from hw.vadim_maletski.func6 import level_11 as vadim_maletski

from .common import qual_name
from .datasets.task_11 import happy_data
from .datasets.task_11 import unhappy_data

solutions = [
    pytest.param(solution, id=qual_name(solution))
    for solution in {  # pylint: disable=use-sequence-for-iteration
        alexander_sidorov,
        siarhei_apanel,
        vadim_maletski,
    }
]


@pytest.mark.parametrize("arg1,arg2", happy_data)
@pytest.mark.parametrize("solution", solutions)
def test_task_11_happy(solution: Any, arg1: Any, arg2: Any) -> None:
    result = solution(arg1, arg2)
    validate_data(result)

    data = result["data"]
    assert isinstance(data, dict)

    assert data == {
        "|a-b|": arg1 ^ arg2,
        "a in b": arg1.issubset(arg2),
        "a-b": arg1 - arg2,
        "a&b": arg1 & arg2,
        "a|b": arg1 | arg2,
        "b in a": arg2.issubset(arg1),
        "b-a": arg2 - arg1,
    }


@pytest.mark.parametrize("arg1,arg2", unhappy_data)
@pytest.mark.parametrize("solution", solutions)
def test_task_11_unhappy(solution: Any, arg1: Any, arg2: Any) -> None:
    result = solution(arg1, arg2)
    validate_errors(result)
