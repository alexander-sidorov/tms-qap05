from datetime import date

from hw.andrey_yelin.lesson06.functions_lesson06hw import age_result_3
from hw.andrey_yelin.lesson06.functions_lesson06hw import decode_7
from hw.andrey_yelin.lesson06.functions_lesson06hw import is_palindrome_1
from hw.andrey_yelin.lesson06.functions_lesson06hw import multiply_args_2
from hw.andrey_yelin.lesson06.functions_lesson06hw import older_4
from hw.andrey_yelin.lesson06.functions_lesson06hw import older_4_v_lambda
from hw.andrey_yelin.lesson06.functions_lesson06hw import parse_http_query_6
from hw.andrey_yelin.lesson06.functions_lesson06hw import repeating_elements_5


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
