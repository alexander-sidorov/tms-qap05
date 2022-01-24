from datetime import date

from hw.andrey_yelin.lesson06.functions_lesson06hw import age_result_3
from hw.andrey_yelin.lesson06.functions_lesson06hw import (
    all_actions_with_two_sets_11,
)
from hw.andrey_yelin.lesson06.functions_lesson06hw import code_8
from hw.andrey_yelin.lesson06.functions_lesson06hw import decode_7
from hw.andrey_yelin.lesson06.functions_lesson06hw import (
    even_keys_and_odd_values_12,
)
from hw.andrey_yelin.lesson06.functions_lesson06hw import is_palindrome_1
from hw.andrey_yelin.lesson06.functions_lesson06hw import multiply_args_2
from hw.andrey_yelin.lesson06.functions_lesson06hw import older_4
from hw.andrey_yelin.lesson06.functions_lesson06hw import older_4_v_lambda
from hw.andrey_yelin.lesson06.functions_lesson06hw import parse_http_query_6
from hw.andrey_yelin.lesson06.functions_lesson06hw import repeating_elements_5
from hw.andrey_yelin.lesson06.functions_lesson06hw import reversed_dictionary_9


def test_is_palindrome_1() -> None:
    assert is_palindrome_1("") == {"data": True}
    assert is_palindrome_1("x") == {"data": True}
    assert is_palindrome_1("xx") == {"data": True}
    assert is_palindrome_1("xy") == {"data": False}
    assert is_palindrome_1(None) == {"errors": "none argument"}
    assert is_palindrome_1(1) == {"errors": "not a string"}


def test_multiply_args_2() -> None:
    assert multiply_args_2(1) == {"data": 1}
    assert multiply_args_2(1, 2) == {"data": 2}
    assert multiply_args_2(1, 2, 3) == {"data": 6}
    assert multiply_args_2() == {"errors": "empty arguments"}
    assert multiply_args_2(1, "a") == {"errors": "variable is not a number"}


def test_age_result_3() -> None:
    date_variable = date(year=1987, month=8, day=2)
    assert age_result_3(date_variable) == {
        "data": {"year": 1987, "month": 8, "day": 2, "age": 34}
    }
    assert age_result_3(2) == {"errors": "variable is not a date"}


def test_older_4() -> None:
    birthday = {
        "A": date(year=2021, month=7, day=18),
        "B": date(year=1993, month=6, day=27),
        "C": date(year=2000, month=3, day=22),
    }
    assert older_4(birthday) == {"data": "B"}
    assert older_4([]) == {"errors": "empty variable"}
    assert older_4({}) == {"errors": "empty variable"}


def test_older_4_v_lambda() -> None:
    birthday = {
        "A": date(year=2021, month=7, day=18),
        "B": date(year=1993, month=6, day=27),
    }
    assert older_4_v_lambda(birthday) == {"data": "B"}
    assert older_4_v_lambda([]) == {"errors": "empty variable"}  # type: ignore
    assert older_4_v_lambda({}) == {"errors": "empty variable"}


def test_repeating_elements_5() -> None:
    elements = [(), "", "", 1]
    assert repeating_elements_5(elements) == {"data": {"": 2}}


def test_parse_http_query_6() -> None:
    http_query = "x=1&x=2&y=3"
    assert parse_http_query_6(http_query) == {
        "data": {"x": ["1", "2"], "y": ["3"]}
    }
    assert parse_http_query_6(None) == {"errors": "none argument"}
    assert parse_http_query_6((1, 2)) == {"errors": "variable is not a string"}
    assert parse_http_query_6("") == {"errors": "empty string"}


def test_decode_7() -> None:
    deco7 = "a11b2c3"
    assert decode_7(deco7) == {"data": "aaaaaaaaaaabbccc"}
    assert decode_7("a1b") == {"errors": "letters is not equal numbers"}


def test_code_8() -> None:
    assert code_8("aaabb") == {"data": "a3b2"}
    assert code_8("aaabba") == {"data": "a3b2a1"}
    assert code_8("") == {"errors": "number of letters = 0"}


def test_reversed_dictionary_9() -> None:
    assert reversed_dictionary_9({1: 100, 2: 100, 3: 300}) == {  # noqa: JS101
        "data": {100: [1, 2], 300: 3}
    }
    assert reversed_dictionary_9("") == {"errors": "argument is not a dict"}
    assert reversed_dictionary_9([]) == {"errors": "argument is not a dict"}
    assert reversed_dictionary_9(()) == {"errors": "argument is not a dict"}


def test_all_actions_with_two_sets_11() -> None:
    assert all_actions_with_two_sets_11({1, 2}, {1, 3}) == {  # noqa: JS101
        "data": {
            "a&b": {1},
            "a|b": {1, 2, 3},
            "a-b": {2},
            "b-a": {3},
            "|a-b|": {2, 3},
            "a in b": False,
            "b in a": False,
        }
    }
    assert all_actions_with_two_sets_11({1, 2}, {1, 2, 3}) == {  # noqa: JS101
        "data": {
            "a&b": {1, 2},
            "a|b": {1, 2, 3},
            "a-b": set(),
            "b-a": {3},
            "|a-b|": {3},
            "a in b": True,
            "b in a": False,
        }
    }
    assert all_actions_with_two_sets_11(123, {1, 2, 3}) == {  # noqa: JS101
        "errors": "first argument has not a set type"
    }
    assert all_actions_with_two_sets_11({1, 2, 3}, 123) == {  # noqa: JS101
        "errors": "second argument has not a set type"
    }


def test_even_keys_and_odd_values_12() -> None:
    assert even_keys_and_odd_values_12(1, 2) == {"data": {1: 2}}
    assert even_keys_and_odd_values_12(1, 2, 3, 4, 5) == {
        "errors": "quantity of arguments is not even"
    }
