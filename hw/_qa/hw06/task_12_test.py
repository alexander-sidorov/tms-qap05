from typing import Any

import pytest

from hw._qa.hw06.common import validate_data
from hw._qa.hw06.common import validate_errors
from hw.alexander_sidorov.lesson06.task12 import task_12 as alexander_sidorov
from hw.andrey_yelin.lesson06.functions_lesson06hw import (
    even_keys_and_odd_values_12 as andrey_yelin,
)
from hw.siarhei_apanel.refakt import diction as siarhei_apanel
from hw.vadim_maletski.func6 import level_12 as vadim_maletski

from .common import qual_name
from .datasets.task_12 import happy_data
from .datasets.task_12 import unhappy_data

solutions = [
    pytest.param(solution, id=qual_name(solution))
    for solution in {  # pylint: disable=use-sequence-for-iteration
        alexander_sidorov,
        andrey_yelin,
        siarhei_apanel,
        vadim_maletski,
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
