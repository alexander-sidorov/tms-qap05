from datetime import date

from hw.maksim_ptitski.lesson6_hw import data_multiplication
from hw.maksim_ptitski.lesson6_hw import how_old_are_you
from hw.maksim_ptitski.lesson6_hw import is_the_string_is_the_palindrome
from hw.maksim_ptitski.lesson6_hw import repeated_symbols
from hw.maksim_ptitski.lesson6_hw import the_oldest_one


def test_is_the_string_is_the_palindrome() -> None:
    assert is_the_string_is_the_palindrome("") == {"data": True}
    assert is_the_string_is_the_palindrome(" ") == {"data": True}
    assert is_the_string_is_the_palindrome("x") == {"data": True}
    assert is_the_string_is_the_palindrome("xx") == {"data": True}
    assert is_the_string_is_the_palindrome("abccba") == {"data": True}
    assert is_the_string_is_the_palindrome("xyz") == {"data": False}
    assert is_the_string_is_the_palindrome(123321) == {  # type: ignore
        "errors": "provided argument is not a string"
    }


def test_data_multiplication() -> None:
    assert data_multiplication(1) == {"data": 1}
    assert data_multiplication(1, 2) == {"data": 2}
    assert data_multiplication(1, 2, 3) == {"data": 6}
    assert data_multiplication("abcd", 2) == {"data": "abcdabcd"}
    assert data_multiplication([1, 2, 3], 2) == {"data": [1, 2, 3, 1, 2, 3]}
    assert data_multiplication((1, 2, 3), 3) == {
        "data": (1, 2, 3, 1, 2, 3, 1, 2, 3)
    }
    assert data_multiplication() == {"errors": "must be more than 0 arguments"}
    assert data_multiplication(2, "a") == {"data": "aa"}
    assert data_multiplication(2, [2]) == {"data": [2, 2]}
    assert data_multiplication(2, [2], 2) == {"data": [2, 2, 2, 2]}
    assert "errors" in data_multiplication(2, [2], 2, [2])


def test_how_old_are_you() -> None:
    d1 = date(year=1987, month=8, day=2)
    d2 = date(year=1987, month=1, day=1)
    d3 = date(year=2023, month=1, day=1)
    assert how_old_are_you(d1) == {
        "data": {"year": 1987, "month": 8, "day": 2, "age": 34}
    }
    assert how_old_are_you(d2) == {
        "data": {"year": 1987, "month": 1, "day": 1, "age": 35}
    }
    assert how_old_are_you(198782) == {  # type: ignore
        "errors": "wrong type of provided data"
    }
    assert how_old_are_you(d3) == {"errors": "you're not born yet"}


def test_the_oldest_one() -> None:
    d1 = {
        "A": date(year=1987, month=8, day=2),
        "B": date(year=1950, month=10, day=5),
    }
    d2 = {
        "A": date(year=1987, month=1, day=3),
        "B": date(year=1987, month=2, day=25),
    }
    assert the_oldest_one(d1) == {"data": "B"}
    assert the_oldest_one(d2) == {"data": "A"}
    assert the_oldest_one(151654684) == {  # type: ignore
        "errors": "Given argument is not a dictionary"
    }


def test_repeated_symbols() -> None:
    c1 = [(), "", "", 1]
    c2 = [1, 2, 3]
    c3 = (1, 2, 3, 1, 5, 1)

    assert repeated_symbols(c1) == {"data": {"": 2}}
    assert repeated_symbols(c2) == {"data": {}}
    assert repeated_symbols(c3) == {"data": {1: 3}}
    assert repeated_symbols(9099323) == {
        "errors": "given arguments are not a list, str or tuple"
    }
