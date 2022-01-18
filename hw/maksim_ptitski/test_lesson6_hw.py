from datetime import date

from hw.maksim_ptitski.lesson6_hw import ERROR_NOT_LIST_STR_TUPLE
from hw.maksim_ptitski.lesson6_hw import ERROR_NOT_STRING
from hw.maksim_ptitski.lesson6_hw import ERROR_UNHASHABLE_TYPE
from hw.maksim_ptitski.lesson6_hw import ERROR_WRONG_FORMAT_OF_STR
from hw.maksim_ptitski.lesson6_hw import count_chars
from hw.maksim_ptitski.lesson6_hw import data_multiplication
from hw.maksim_ptitski.lesson6_hw import how_old_are_you
from hw.maksim_ptitski.lesson6_hw import http_query
from hw.maksim_ptitski.lesson6_hw import inverted_dictionary
from hw.maksim_ptitski.lesson6_hw import is_the_string_is_the_palindrome
from hw.maksim_ptitski.lesson6_hw import make_dictionary
from hw.maksim_ptitski.lesson6_hw import relations_between_two_sets
from hw.maksim_ptitski.lesson6_hw import repeat_chars
from hw.maksim_ptitski.lesson6_hw import repeated_symbols
from hw.maksim_ptitski.lesson6_hw import the_oldest_one
from hw.maksim_ptitski.lesson6_hw import zip_collections_to_dict


def test_is_the_string_is_the_palindrome() -> None:
    assert is_the_string_is_the_palindrome("") == {"data": True}
    assert is_the_string_is_the_palindrome(" ") == {"data": True}
    assert is_the_string_is_the_palindrome("x") == {"data": True}
    assert is_the_string_is_the_palindrome("xx") == {"data": True}
    assert is_the_string_is_the_palindrome("abccba") == {"data": True}
    assert is_the_string_is_the_palindrome("xy") == {"data": False}
    assert is_the_string_is_the_palindrome(123321) == {
        "errors": [ERROR_NOT_STRING]
    }


def test_data_multiplication() -> None:
    assert data_multiplication(1) == {"data": 1}
    assert data_multiplication(1, 2) == {"data": 2}
    assert data_multiplication(1, 2, 3) == {"data": 6}
    assert data_multiplication("abc", 2) == {"data": "abcabc"}
    assert data_multiplication([1, 2, 3], 2) == {"data": [1, 2, 3, 1, 2, 3]}
    assert data_multiplication((1, 2, 3), 2) == {"data": (1, 2, 3, 1, 2, 3)}
    assert data_multiplication() == {"errors": ["no argument is given"]}
    assert data_multiplication("abc", "ab") == {
        "errors": ["given arguments' types can't be multiplied"]
    }
    assert data_multiplication("a", 2) == {"data": "aa"}
    assert data_multiplication(2, [1], 2) == {"data": [1, 1, 1, 1]}
    assert data_multiplication("a") == {"data": "a"}


def test_how_old_are_you() -> None:
    d1 = date(year=1987, month=8, day=2)
    d2 = date(year=1987, month=1, day=2)
    assert how_old_are_you(d1) == {
        "data": {"year": 1987, "month": 8, "day": 2, "age": 34}
    }
    assert how_old_are_you(d2) == {
        "data": {"year": 1987, "month": 1, "day": 2, "age": 35}
    }
    assert how_old_are_you(198782) == {
        "errors": ["given argument is not object of date type"]
    }


def test_the_oldest_one() -> None:
    d1 = {
        "A": date(year=1987, month=8, day=2),
        "B": date(year=1950, month=10, day=5),
    }
    d2 = {
        "A": date(year=1987, month=1, day=3),
        "B": date(year=1987, month=2, day=25),
    }
    d3 = {"A": 198782, "B": 197282}
    assert the_oldest_one(d1) == {"data": "B"}
    assert the_oldest_one(d2) == {"data": "A"}
    assert the_oldest_one(198782) == {
        "errors": ["Given argument is not a dictionary"]
    }
    assert the_oldest_one(d3) == {
        "errors": ["key value is not object of date type"]
    }


def test_repeated_symbols() -> None:
    c1 = [(), "", "", 1]
    c2 = [1, 2, 3]
    c3 = (1, 2, 3, 7, 5, 1)
    c4 = [(), {}, {}, 1]
    c5 = {1, 2, 3, 4, 5}
    c6 = {1: 1, 2: 1, 3: 1, 4: 1, 5: 1}

    assert repeated_symbols(c1) == {"data": {"": 2}}
    assert repeated_symbols(c2) == {"data": {}}
    assert repeated_symbols(c3) == {"data": {1: 2}}
    assert repeated_symbols(123) == {"errors": [ERROR_NOT_LIST_STR_TUPLE]}
    assert repeated_symbols(c4) == {"errors": [ERROR_UNHASHABLE_TYPE]}
    assert repeated_symbols(c5) == {"data": {}}
    assert repeated_symbols(c6) == {"data": {}}


def test_repeat_chars() -> None:
    assert repeat_chars("a3b2c1") == {"data": "aaabbc"}
    assert repeat_chars(["a3b2c1"]) == {
        "errors": ["given argument is not string type"]
    }
    assert repeat_chars("a3b2c") == {"errors": [ERROR_WRONG_FORMAT_OF_STR]}
    assert repeat_chars("13b2c1") == {"errors": [ERROR_WRONG_FORMAT_OF_STR]}
    assert repeat_chars("a3b2cv") == {"errors": [ERROR_WRONG_FORMAT_OF_STR]}
    assert repeat_chars("a11") == {"data": "aaaaaaaaaaa"}
    assert repeat_chars("a1b1a1") == {"data": "aba"}


def test_count_chars() -> None:
    assert count_chars("aaabb") == {"data": "a3b2"}
    assert count_chars("aaabb111!!") == {"data": "a3b213!2"}
    assert count_chars(12345) == {"errors": [ERROR_NOT_STRING]}
    assert count_chars("") == {"data": ""}
    assert count_chars("a") == {"data": "a1"}
    assert count_chars("aba") == {"data": "a1b1a1"}


def test_inverted_dictionary() -> None:
    d1 = {1: 100, 2: 100, 3: 300}
    d2 = {1: {1: 100, 2: 200}, 2: 100, 3: 300}
    assert inverted_dictionary(d1) == {"data": {100: [1, 2], 300: 3}}
    assert inverted_dictionary(1234) == {
        "errors": ["given argument is not dict type"]
    }
    assert inverted_dictionary(d2) == {
        "errors": ["dictionary value contains unhashable type"]
    }
    assert inverted_dictionary({}) == {"data": {}}


def test_zip_collections_to_dict() -> None:
    assert zip_collections_to_dict("abc", [1, 2]) == {
        "data": {"a": 1, "b": 2, "c": None}
    }
    assert zip_collections_to_dict("ab", [1, 2, 3]) == {
        "data": {"a": 1, "b": 2, "...": [3]}
    }
    assert zip_collections_to_dict("abc", [5, 6, 7]) == {
        "data": {"a": 5, "b": 6, "c": 7}
    }
    assert zip_collections_to_dict("abc", 123) == {
        "errors": ["given argument with values is not a list, str or tuple"]
    }
    assert zip_collections_to_dict(123, "abc") == {
        "errors": ["given argument with keys is not a list, str or tuple"]
    }
    assert zip_collections_to_dict(123, 456) == {
        "errors": [
            "given argument with keys is not a list, str or tuple",
            "given argument with values is not a list, str or tuple",
        ]
    }
    assert zip_collections_to_dict(
        [{1: 2}, 4, 5], [1, 2, 3]
    ) == {  # noqa: JS101
        "errors": [ERROR_UNHASHABLE_TYPE]
    }
    assert zip_collections_to_dict([{1: 2}, 4], [1, 2, 3],) == {  # noqa: JS101
        "errors": [ERROR_UNHASHABLE_TYPE]
    }  # noqa: W503
    assert zip_collections_to_dict([{1: 2}, 3, 4], [1, 2],) == {  # noqa: JS101
        "errors": [ERROR_UNHASHABLE_TYPE]
    }  # noqa: W503


def test_relations_between_two_sets() -> None:
    error1 = {"errors": ["given first argument is not set type"]}
    error2 = {"errors": ["given second argument is not set type"]}
    error3 = {
        "errors": [
            "given first argument is not set type",
            "given second argument is not set type",
        ]
    }
    assert relations_between_two_sets({1, 2}, {1, 3}) == {  # noqa: JS101
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
    assert relations_between_two_sets({1, 2}, {1, 2, 3}) == {  # noqa: JS101
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
    assert relations_between_two_sets(123, {1, 2, 3}) == error1
    assert relations_between_two_sets({1, 2, 3}, 123) == error2
    assert relations_between_two_sets(123, 123) == error3


def test_make_dictionary() -> None:
    assert make_dictionary(1, 2) == {"data": {1: 2}}
    assert make_dictionary(1, 2, 3) == {
        "errors": ["Quantity of given arguments is not even"]
    }
    assert make_dictionary({1: 2, 2: 3}, 5) == {  # noqa: JS101
        "errors": ["odd argument is unhashable type"]
    }


def test_http_query() -> None:
    assert http_query("x=1&x=2&y=3") == {"data": {"x": ["1", "2"], "y": ["3"]}}
    assert http_query("xyz=123&xyz=abc&qqq=348") == {
        "data": {"xyz": ["123", "abc"], "qqq": ["348"]}
    }
    assert http_query("x=&x=2&q=3") == {"data": {"x": ["", "2"], "q": ["3"]}}
    assert http_query(["x=1&x=2&y=3"]) == {"errors": [ERROR_NOT_STRING]}
    assert http_query("x=1&&x=2&q=3") == {
        "errors": ["given query contains wrong format"]
    }
    assert http_query("xxx=&yyy=") == {"data": {"xxx": [""], "yyy": [""]}}
