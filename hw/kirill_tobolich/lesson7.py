import pytest
from typing import Callable
from hw.kirill_tobolich.lesson6_hw import palindrome
from hw.kirill_tobolich.lesson6_hw import multiply
from hw.kirill_tobolich.validate_func import validate
from hw.kirill_tobolich.validate_func import Undefined


# functions = palindrome


# dataset = [
#     ([""], True),
#     ([" "], True),
#     (["xx"], True),
#     (["abccba"], True),
#     (["xy"], False),
#     ([123321], Undefined),
#     ([None], Undefined),
#     (["  abc"], False)
# ]


# @pytest.mark.parametrize("func", functions)
# @pytest.mark.parametrize("data", dataset)
# def test_validate(func: Callable, data: list):
#     args, expected = data
#     if expected is not Undefined:
#         validate(func, *args, expected_data=expected)
#     else:
#         validate(func, *args, expected_errors=[])

functions = [palindrome, multiply]


dataset = [
    (functions[0], [""], True),
    (functions[0], [" "], True),
    (functions[0], ["xx"], True),
    (functions[0], ["abccba"], True),
    (functions[0], ["xy"], False),
    (functions[0], [123321], Undefined),
    (functions[0], [None], Undefined),
    (functions[0], ["  abc"], False),
    (functions[1], [1, 2], 2)
]


@pytest.mark.parametrize("func, data, expected", dataset)
def test_validate(func: Callable, data: list, expected):

    if expected is not Undefined:
        validate(func, *data, expected_data=expected)
    else:
        validate(func, *data, expected_errors=[])