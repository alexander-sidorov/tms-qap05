from datetime import date

from hw.kirill_tobolich.lesson6_hw import ERROR_NOT_STRING
from hw.kirill_tobolich.lesson6_hw import count_chars
from hw.kirill_tobolich.lesson6_hw import get_formatted_birthday
from hw.kirill_tobolich.lesson6_hw import get_the_eldest
from hw.kirill_tobolich.lesson6_hw import get_the_same_elements_in_collection
from hw.kirill_tobolich.lesson6_hw import http_query_parser
from hw.kirill_tobolich.lesson6_hw import inverted_dictionary
from hw.kirill_tobolich.lesson6_hw import make_dictionary
from hw.kirill_tobolich.lesson6_hw import multiply
from hw.kirill_tobolich.lesson6_hw import palindrome
from hw.kirill_tobolich.lesson6_hw import relations_between_two_sets
from hw.kirill_tobolich.lesson6_hw import repeat_chars
from hw.kirill_tobolich.lesson6_hw import zip_collections_to_dict


def test_palindrome() -> None:
    assert palindrome("") == {"data": True}
    assert palindrome(" ") == {"data": True}
    assert palindrome("x") == {"data": True}
    assert palindrome("xx") == {"data": True}
    assert palindrome("abccba") == {"data": True}
    assert palindrome("xy") == {"data": False}
    assert palindrome(123321) == {"errors": [ERROR_NOT_STRING]}


def test_multiply() -> None:
    assert multiply(1) == {"data": 1}
    assert multiply(1, 2) == {"data": 2}
    assert multiply(1, 2, 3) == {"data": 6}
    assert multiply("abc", 2) == {"data": "abcabc"}
    assert multiply([1, 2, 3], 2) == {"data": [1, 2, 3, 1, 2, 3]}
    assert multiply((1, 2, 3), 2) == {"data": (1, 2, 3, 1, 2, 3)}
    assert multiply() == {"errors": ["no argument is given"]}
    assert multiply("abc", "ab") == {
        "errors": ["given arguments' types can't be multiplied"]
    }
    assert multiply("a", 2) == {"data": "aa"}
    assert multiply(2, [1], 2) == {"data": [1, 1, 1, 1]}
    assert multiply("a") == {"data": "a"}


def test_get_formatted_birthday() -> None:
    d1 = date(year=1987, month=8, day=2)
    d2 = date(year=1987, month=1, day=2)
    assert get_formatted_birthday(d1) == {
        "data": {"year": 1987, "month": 8, "day": 2, "age": 34}
    }
    assert get_formatted_birthday(d2) == {
        "data": {"year": 1987, "month": 1, "day": 2, "age": 35}
    }
    assert get_formatted_birthday(198782) == {
        "errors": ["given argument is not object of date type"]
    }


def test_get_the_eldest() -> None:
    d1 = {
        "A": date(year=1987, month=8, day=2),
        "B": date(year=1950, month=10, day=5),
    }
    d2 = {
        "A": date(year=1987, month=1, day=3),
        "B": date(year=1987, month=2, day=25),
    }
    d3 = {"A": 198782, "B": 197282}
    assert get_the_eldest(d1) == {"data": "B"}
    assert get_the_eldest(d2) == {"data": "A"}
    assert get_the_eldest(198782) == {
        "errors": ["Given argument is not a dictionary"]
    }
    assert get_the_eldest(d3) == {
        "errors": ["key value is not object of date type"]
    }


def test_get_the_same_elements_in_collection() -> None:
    c1 = [(), "", "", 1]
    c2 = [1, 2, 3]
    c3 = (1, 2, 3, 7, 5, 1)
    c4 = [(), {}, {}, 1]
    c5 = {1, 2, 3, 4, 5}
    c6 = {1: 1, 2: 1, 3: 1, 4: 1, 5: 1}

    assert get_the_same_elements_in_collection(c1) == {"data": {"": 2}}
    assert get_the_same_elements_in_collection(c2) == {"data": {}}
    assert get_the_same_elements_in_collection(c3) == {"data": {1: 2}}
    assert get_the_same_elements_in_collection(123) == {
        "errors": ["given argument with keys is not a list, str or tuple"]
    }
    assert get_the_same_elements_in_collection(c4) == {
        "errors": ["collection contains unhashable type"]
    }
    assert get_the_same_elements_in_collection(c5) == {"data": {}}
    assert get_the_same_elements_in_collection(c6) == {"data": {}}


def test_http_query_parser() -> None:
    assert http_query_parser("x=1&x=2&y=3") == {
        "data": {"x": ["1", "2"], "y": ["3"]}
    }
    assert http_query_parser("xyz=123&xyz=abc&qqq=348") == {
        "data": {"xyz": ["123", "abc"], "qqq": ["348"]}
    }
    assert http_query_parser("x=&x=2&q=3") == {
        "data": {"x": ["", "2"], "q": ["3"]}
    }
    assert http_query_parser(["x=1&x=2&y=3"]) == {"errors": [ERROR_NOT_STRING]}
    assert http_query_parser("x=1&&x=2&q=3") == {
        "errors": ["given query contains wrong format"]
    }
    assert http_query_parser("xxx=&yyy=") == {
        "data": {"xxx": [""], "yyy": [""]}
    }


def test_repeat_chars() -> None:
    assert repeat_chars("a3b2c1") == {"data": "aaabbc"}
    assert repeat_chars(["a3b2c1"]) == {
        "errors": ["given argument is not string type"]
    }
    assert repeat_chars("a3b2c") == {"errors": ["wrong format of string"]}
    assert repeat_chars("13b2c1") == {"errors": ["wrong format of string"]}
    assert repeat_chars("a3b2cv") == {"errors": ["wrong format of string"]}
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
        "errors": ["collections contain values with unhashable type"]
    }
    assert zip_collections_to_dict([{1: 2}, 4], [1, 2, 3],) == {  # noqa: JS101
        "errors": ["collections contain values with unhashable type"]
    }  # noqa: W503
    assert zip_collections_to_dict([{1: 2}, 3, 4], [1, 2],) == {  # noqa: JS101
        "errors": ["collections contain values with unhashable type"]
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
