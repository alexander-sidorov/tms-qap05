from collections import defaultdict
from datetime import date
from datetime import datetime
from random import choice  # noqa: DUO102,S311
from string import ascii_letters
from typing import Any
from typing import Dict

from hw.maria_saganovich.lesson6_hw.lvl1_palindrome import func1_palindrome
from hw.maria_saganovich.lesson6_hw.lvl2_product import func2_product
from hw.maria_saganovich.lesson6_hw.lvl3_age import func3_age
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


class SuperStr(str):
    pass


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
    assert func1_palindrome(SuperStr("aaa")) == {"data": True}


def test_task_02() -> None:
    assert func2_product((1,), 2) == {"data": (1, 1)}
    assert func2_product(2, (1,)) == {"data": (1, 1)}
    assert func2_product(2, "a", 2) == {"data": "aaaa"}

    validate_errors(func2_product(2, "a", (2,)))
    validate_errors(func2_product((), "a"))


def test_task_03() -> None:
    atm = datetime.now().replace(year=2000, month=1, day=1)
    assert func3_age(atm.date())["data"]["year"] == 2000
    assert func3_age(atm)["data"]["year"] == 2000


def test_task_04() -> None:
    validate_errors(func4_oldest(Typ()))

    d1 = date(2000, 1, 1)
    d2 = datetime.now().replace(year=1990, month=1, day=1)

    data = {(): d1, frozenset(): d2}
    assert func4_oldest(data) == {"data": [frozenset()]}

    data = defaultdict(None, data)
    assert func4_oldest(data) == {"data": [frozenset()]}


def test_task_05() -> None:
    validate_errors(func5_duplicate_elements(Typ()))

    assert func5_duplicate_elements(()) == {"data": {}}
    assert func5_duplicate_elements((1, 1)) == {"data": {1: 2}}
    assert func5_duplicate_elements([1, 1]) == {"data": {1: 2}}
    assert func5_duplicate_elements([]) == {"data": {}}
    assert func5_duplicate_elements(defaultdict(None)) == {"data": {}}
    assert func5_duplicate_elements(range(10)) == {"data": {}}
    assert func5_duplicate_elements({1, 2, 3}) == {"data": {}}
    assert func5_duplicate_elements({}) == {"data": {}}

    for typ in (dict, set, frozenset):
        validate_errors(func5_duplicate_elements([typ()]))


def test_task_06() -> None:
    validate_errors(func6_dict_http_query(Typ()))

    assert func6_dict_http_query(SuperStr("xx=&y=&z=1&z=2")) == {
        "data": {
            "xx": [""],
            "y": [""],
            "z": ["1", "2"],
        }
    }


def test_task_07() -> None:
    assert func7_str_duplicate_char("") == {"data": ""}
    assert func7_str_duplicate_char("a11b1a1") == {"data": "aaaaaaaaaaaba"}
    assert func7_str_duplicate_char(SuperStr("")) == {"data": ""}
    assert func7_str_duplicate_char("¹2") == {"data": "¹¹"}


def test_task_08() -> None:
    assert func8_duplicate_char_number("") == {"data": ""}
    assert func8_duplicate_char_number("aaaaaaaaaaaba") == {"data": "a11b1a1"}
    assert func8_duplicate_char_number(SuperStr("")) == {"data": ""}
    validate_errors(func8_duplicate_char_number("1"))
    validate_errors(func8_duplicate_char_number("aaa3"))
    validate_errors(func8_duplicate_char_number(Typ()))


def test_task_09() -> None:
    assert func9_swap_keys_values({}) == {"data": {}}
    assert func9_swap_keys_values({1: 100}) == {"data": {100: [1]}}
    assert func9_swap_keys_values({"a": ...}) == {"data": {...: ["a"]}}
    assert func9_swap_keys_values({"a": ..., "b": ...}) == {  # noqa: JS101
        "data": {...: ["a", "b"]},
    }

    arg: Any = defaultdict(None)
    assert func9_swap_keys_values(arg) == {"data": {}}

    validate_errors(func9_swap_keys_values(Typ()))
    validate_errors(func9_swap_keys_values({1: [], 2: {}}))
    validate_errors(func9_swap_keys_values({1: [1], 2: {2: 2}}))


def test_task_10() -> None:
    types: Any = (list, str, tuple)
    for typ1 in types:
        for typ2 in types:
            arg1 = typ1()
            arg2 = typ2()
            assert func10_empty_keys_values(arg1, arg2) == {"data": {}}

            arg1 = typ1("1")
            arg2 = typ2("2")
            assert func10_empty_keys_values(arg1, arg2) == {"data": {"1": "2"}}

    types = (dict, set, frozenset)
    for typ1 in types:
        for typ2 in types:
            arg1 = typ1()
            arg2 = typ2()
            validate_errors(func10_empty_keys_values(arg1, arg2))


def test_task_12() -> None:
    validate_errors(func12_even_keys_odd_values(1))
    validate_errors(func12_even_keys_odd_values(*"abc"))
    validate_errors(func12_even_keys_odd_values([], {}))
    validate_errors(func12_even_keys_odd_values({}, []))
    validate_errors(func12_even_keys_odd_values(set(), 1))
    validate_errors(func12_even_keys_odd_values(frozenset(), 1))

    assert func12_even_keys_odd_values(1, 2) == {"data": {1: 2}}
    assert func12_even_keys_odd_values(1, 2, 3, 4) == {"data": {1: 2, 3: 4}}
    assert func12_even_keys_odd_values(..., ..., Typ, type) == {
        "data": {...: ..., Typ: type}
    }
