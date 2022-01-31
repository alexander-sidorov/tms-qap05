from typing import Any

import pytest

from hw._qa.hw06.common import validate_data
from hw._qa.hw06.common import validate_errors
from hw.alexander_sidorov.lesson06.task02 import task_02 as alexander_sidorov
from hw.siarhei_apanel.refakt import proizvedenie as siarhei_apanel
from hw.vadim_maletski.func6 import level_02 as vadim_maletski
from hw.nikita_pakhomov.nlesson3.hw6 import level_2 as nikita_pakhomov

from .common import qual_name
from .datasets.task_02 import happy_data
from .datasets.task_02 import unhappy_data

solutions = [
    pytest.param(solution, id=qual_name(solution))
    for solution in {  # pylint: disable=use-sequence-for-iteration
        alexander_sidorov,
        nikita_pakhomov,
        siarhei_apanel,
        vadim_maletski,
    }
]


@pytest.mark.parametrize("args,expected", happy_data)
@pytest.mark.parametrize("solution", solutions)
def test_task_02_happy(solution: Any, args: Any, expected: Any) -> None:
    result = solution(*args)
    validate_data(result)

    data = result["data"]
    assert data == expected


@pytest.mark.parametrize("args", unhappy_data)
@pytest.mark.parametrize("solution", solutions)
def test_task_02_unhappy(solution: Any, args: Any) -> None:
    result = solution(*args)
    validate_errors(result)
