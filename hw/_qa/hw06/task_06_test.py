from typing import Any

import pytest

from hw._qa.hw06.common import validate_data
from hw._qa.hw06.common import validate_errors
from hw.alexander_sidorov.lesson06.task06 import task_06 as alexander_sidorov
from hw.kirill_tobolich.lesson6_hw import http_query_parser as kirill_tobolich
from hw.maria_saganovich.lesson6_hw.lvl6_dict_http_query import (
    func6_dict_http_query as maria_saganovich,
)
from hw.siarhei_apanel.refakt import html_str as siarhei_apanel
from hw.vadim_maletski.func6 import level_06 as vadim_maletski

from .common import qual_name
from .datasets.task_06 import happy_data
from .datasets.task_06 import unhappy_data

solutions = [
    pytest.param(solution, id=qual_name(solution))
    for solution in {  # pylint: disable=use-sequence-for-iteration
        alexander_sidorov,
        kirill_tobolich,
        maria_saganovich,
        siarhei_apanel,
        vadim_maletski,
    }
]


@pytest.mark.parametrize("arg,expected", happy_data)
@pytest.mark.parametrize("solution", solutions)
def test_task_06_happy(solution: Any, arg: Any, expected: Any) -> None:
    result = solution(arg)
    validate_data(result)

    data = result["data"]
    assert data == expected


@pytest.mark.parametrize("arg", unhappy_data)
@pytest.mark.parametrize("solution", solutions)
def test_task_06_unhappy(solution: Any, arg: Any) -> None:
    result = solution(arg)
    validate_errors(result)
