from typing import Any

import pytest

from hw._qa.hw06.common import validate_data
from hw._qa.hw06.common import validate_errors
from hw.alexander_sidorov.lesson06.task03 import task_03 as alexander_sidorov
from hw.maria_saganovich.lesson6_hw.lvl3_age import (
    func3_age as maria_saganovich,
)

from .common import azaza
from .common import qual_name
from .datasets.task_03 import happy_data
from .datasets.task_03 import unhappy_data

solutions = [
    pytest.param(solution, id=qual_name(solution))
    for solution in {  # pylint: disable=use-sequence-for-iteration
        alexander_sidorov,
        maria_saganovich,
    }
]


@pytest.mark.parametrize("arg,expected", happy_data)
@pytest.mark.parametrize("solution", solutions)
def test_task_03_happy(solution: Any, arg: Any, expected: Any) -> None:
    result = solution(arg)
    validate_data(result)

    data = result["data"]
    assert isinstance(data, dict)

    keys = {"year", "month", "day", "age"}
    aza = azaza()
    for key in keys:
        assert (value := data.get(key, aza)) is not aza
        assert isinstance(value, int)

    age = data["age"]
    assert age == expected


@pytest.mark.parametrize("arg", unhappy_data)
@pytest.mark.parametrize("solution", solutions)
def test_task_03_unhappy(solution: Any, arg: Any) -> None:
    result = solution(arg)
    validate_errors(result)
