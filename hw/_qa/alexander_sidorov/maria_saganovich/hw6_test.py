from datetime import date
from random import choice  # noqa: DUO102,S311
from string import ascii_letters
from typing import Dict

from hw.maria_saganovich.lesson6_hw.lvl1_palindrome import func1_palindrome
from hw.maria_saganovich.lesson6_hw.lvl2_product import func2_product
from hw.maria_saganovich.lesson6_hw.lvl4_oldest import func4_oldest
from hw.maria_saganovich.lesson6_hw.lvl5_duplicate_elements import (
    func5_duplicate_elements,
)
from hw.maria_saganovich.lesson6_hw.lvl6_dict_http_query import (
    func6_dict_http_query,
)
from hw.maria_saganovich.lesson6_hw.lvl7_str_duplicate_char import (
    func7_str_duplicate_char,
)
from hw.maria_saganovich.lesson6_hw.lvl8_duplicate_char_number import (
    func8_duplicate_char_number,
)
from hw.maria_saganovich.lesson6_hw.lvl9_swap_keys_values import (
    func9_swap_keys_values,
)
from hw.maria_saganovich.lesson6_hw.lvl10_empty_keys_values import (
    func10_empty_keys_values,
)
from hw.maria_saganovich.lesson6_hw.lvl12_even_keys_odd_values import (
    func12_even_keys_odd_values,
)

Typ = type(
    "".join(choice(ascii_letters) for _ in range(10)), (), {}  # noqa: S311
)


def validate_errors(result: Dict) -> None:
    assert isinstance(result, dict)
    errors = result.get("errors")
    assert errors
    assert isinstance(errors, list)
    for error in errors:
        assert isinstance(error, str)
    assert errors == sorted(errors)


def test_task_01() -> None:
    assert func1_palindrome("a   a a") == {"data": False}
    assert func1_palindrome("Aaa") == {"data": False}
    assert func1_palindrome("aaa") == {"data": True}


def test_task_02() -> None:
    assert func2_product((1,), 2) == {"data": (1, 1)}
    assert func2_product(2, (1,)) == {"data": (1, 1)}
    assert func2_product(2, "a", 2) == {"data": "aaaa"}

    validate_errors(func2_product(2, "a", (2,)))


def test_task_04() -> None:
    validate_errors(func4_oldest(Typ()))

    d1 = date(2000, 1, 1)
    d2 = date(1990, 1, 1)

    data = {(): d1, frozenset(): d2}

    assert func4_oldest(data) == {"data": [frozenset()]}


def test_task_05() -> None:
    validate_errors(func5_duplicate_elements(Typ()))

    assert func5_duplicate_elements({}) == {"data": {}}
    assert func5_duplicate_elements([]) == {"data": {}}
    assert func5_duplicate_elements(()) == {"data": {}}

    validate_errors(func5_duplicate_elements([{}, set()]))


def test_task_06() -> None:
    validate_errors(func6_dict_http_query(Typ()))


def test_task_07() -> None:
    assert func7_str_duplicate_char("") == {"data": ""}
    assert func7_str_duplicate_char("a11b1a1") == {"data": "aaaaaaaaaaaba"}


def test_task_08() -> None:
    assert func8_duplicate_char_number("") == {"data": ""}
    assert func8_duplicate_char_number("aaaaaaaaaaaba") == {"data": "a11b1a1"}
    validate_errors(func8_duplicate_char_number(Typ()))
    validate_errors(func8_duplicate_char_number("1"))
    validate_errors(func8_duplicate_char_number("aaa3"))


def test_task_09() -> None:
    validate_errors(func9_swap_keys_values(Typ()))
    validate_errors(func9_swap_keys_values({1: [], 2: {}}))


def test_task_10() -> None:
    types = (list, str, tuple)
    for typ1 in types:
        for typ2 in types:
            arg1 = typ1()
            arg2 = typ2()
            assert func10_empty_keys_values(arg1, arg2) == {"data": {}}


def test_task_12() -> None:
    validate_errors(func12_even_keys_odd_values(1))
    validate_errors(func12_even_keys_odd_values(*"abc"))

    assert func12_even_keys_odd_values(1, 2) == {"data": {1: 2}}
    assert func12_even_keys_odd_values(1, 2, 3, 4) == {"data": {1: 2, 3: 4}}
    assert func12_even_keys_odd_values(..., ..., Typ, type) == {
        "data": {...: ..., Typ: type}
    }
