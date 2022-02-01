from typing import Any

import pytest

from hw._qa.hw06.common import validate_data
from hw._qa.hw06.common import validate_errors
from hw.alexander_sidorov.lesson06.task01 import task_01 as alexander_sidorov
from hw.maksim_ptitski.lesson6_hw import palindrome as maksim_ptitski
from hw.maria_saganovich.lesson6_hw.lvl1_palindrome import (
    func1_palindrome as maria_saganovich,
)
from hw.siarhei_apanel.refakt import palindrom as siarhei_apanel
from hw.vadim_maletski.func6 import level_01 as vadim_maletski

from .common import qual_name
from .datasets.task_01 import happy_data
from .datasets.task_01 import unhappy_data

solutions = [
    pytest.param(solution, id=qual_name(solution))
    for solution in {  # pylint: disable=use-sequence-for-iteration
        alexander_sidorov,
        maksim_ptitski,
        maria_saganovich,
        siarhei_apanel,
        vadim_maletski,
    }
]


@pytest.mark.parametrize("arg,expected", happy_data)
@pytest.mark.parametrize("solution", solutions)
def test_task_01_happy(solution: Any, arg: Any, expected: Any) -> None:
    result = solution(arg)
    validate_data(result)

    data = result["data"]
    assert data == expected


@pytest.mark.parametrize("arg", unhappy_data)
@pytest.mark.parametrize("solution", solutions)
def test_task_01_unhappy(solution: Any, arg: Any) -> None:
    result = solution(arg)
    validate_errors(result)
