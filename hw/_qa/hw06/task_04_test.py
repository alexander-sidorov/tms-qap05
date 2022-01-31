from typing import Any

import pytest

from hw._qa.hw06.common import validate_data
from hw._qa.hw06.common import validate_errors
from hw.alexander_sidorov.lesson06.task04 import task_04 as alexander_sidorov
from hw.siarhei_apanel.refakt import happybithday as siarhei_apanel
from hw.vadim_maletski.func6 import level_04 as vadim_maletski
from hw.nikita_pakhomov.nlesson3.hw6 import level_4_1 as nikita_pakhomov

from .common import qual_name
from .datasets.task_04 import happy_data
from .datasets.task_04 import unhappy_data

solutions = [
    pytest.param(solution, id=qual_name(solution))
    for solution in {  # pylint: disable=use-sequence-for-iteration
        alexander_sidorov,
        nikita_pakhomov,
        siarhei_apanel,
        vadim_maletski,
    }
]


@pytest.mark.parametrize("arg,expected", happy_data)
@pytest.mark.parametrize("solution", solutions)
def test_task_04_happy(solution: Any, arg: Any, expected: Any) -> None:
    result = solution(arg)
    validate_data(result)

    data = result["data"]
    assert data == expected


@pytest.mark.parametrize("arg", unhappy_data)
@pytest.mark.parametrize("solution", solutions)
def test_task_04_unhappy(solution: Any, arg: Any) -> None:
    result = solution(arg)
    validate_errors(result)
