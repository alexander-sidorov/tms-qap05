from datetime import date

from hw.valeriya_mavritskaya.lesson06.homework06_functions import birthday_3
from hw.valeriya_mavritskaya.lesson06.homework06_functions import (
    count_amount_8,
)
from hw.valeriya_mavritskaya.lesson06.homework06_functions import (
    dict_from_http_6,
)
from hw.valeriya_mavritskaya.lesson06.homework06_functions import duplicates_5
from hw.valeriya_mavritskaya.lesson06.homework06_functions import (
    if_palindrome_1,
)
from hw.valeriya_mavritskaya.lesson06.homework06_functions import (
    join_dictionary_10,
)
from hw.valeriya_mavritskaya.lesson06.homework06_functions import (
    mk_dictionary_12,
)
from hw.valeriya_mavritskaya.lesson06.homework06_functions import (
    multiplication_2,
)
from hw.valeriya_mavritskaya.lesson06.homework06_functions import oldest_4
from hw.valeriya_mavritskaya.lesson06.homework06_functions import (
    repeated_symbols_7,
)
from hw.valeriya_mavritskaya.lesson06.homework06_functions import (
    revert_dictionary_9,
)
from hw.valeriya_mavritskaya.lesson06.homework06_functions import (
    set_operations_11,
)


def test_if_palindrome_1() -> None:
    assert if_palindrome_1("") == {"data": "This is a palindrome"}
    assert if_palindrome_1("x") == {"data": "This is a palindrome"}
    assert if_palindrome_1("xx") == {"data": "This is a palindrome"}
    assert if_palindrome_1("xy") == {"data": "This is not a palindrome"}
    assert if_palindrome_1(True) == {"error": "Input must be a string"}
    assert if_palindrome_1("А муза рада музе без ума да разума") == {
        "data": "This is a palindrome"
    }


def test_multiplication_2() -> None:
    assert multiplication_2(1) == {"data": 1}
    assert multiplication_2(1, 2) == {"data": 2}
    assert multiplication_2(1, 2, 3) == {"data": 6}
    assert multiplication_2(1, 2, 3, 8) == {"data": 48}
    assert multiplication_2(1, 2, 3, "dd") == {
        "error": "Input must be a number"
    }


def test_birthday_3() -> None:
    assert birthday_3(date(year=1987, month=8, day=2)) == {
        "year": 1987,
        "month": 8,
        "day": 2,
        "age": 34,
    }
    assert birthday_3("1987") == {"error": "Input must be a date"}  # type: ignore  # noqa: E501


def test_oldest_4() -> None:
    assert oldest_4(
        {
            "A": date(year=2000, month=5, day=4),
            "B": date(year=1855, month=4, day=3),
        }
    ) == {
        "data": "B"
    }  # noqa: W503
    assert oldest_4(
        {"A": date(1993, 8, 3), "B": date(2000, 6, 6), "C": date(1980, 4, 5)}
    ) == {"data": "C"}


def test_duplicates_5() -> None:
    assert duplicates_5([(), "", "", 1]) == {"data": {"": 2}}


def test_dict_from_http_6() -> None:
    assert dict_from_http_6("x=1&x=2&y=3") == {
        "data": {"x": ["1", "2"], "y": ["3"]}
    }


def test_repeated_symbols_7() -> None:
    assert repeated_symbols_7("a3b2c1") == {"data": "aaabbc"}
    assert repeated_symbols_7(False) == {"error": "Invalid input"}  # type: ignore  # noqa: E501


def test_count_amount_8() -> None:
    assert count_amount_8("aaabb") == {"data": "a3b2"}
    assert count_amount_8(False) == {"error": "Invalid input"}  # type: ignore


def test_revert_dictionary_9() -> None:
    assert revert_dictionary_9({1: 100, 2: 100, 3: 300}) == {  # noqa: JS101
        "data": {100: [1, 2], 300: 3}
    }


def test_join_dictionary_10() -> None:
    assert join_dictionary_10("abc", [1, 2]) == {
        "data": {"a": 1, "b": 2, "c": None}
    }
    assert join_dictionary_10("ab", [1, 2, 3]) == {
        "data": {"a": 1, "b": 2, ...: [3]}
    }


def test_set_operations_11() -> None:
    assert set_operations_11({1, 2}, {1, 3}) == {  # noqa: JS101
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


def test_mk_dictionary_12() -> None:
    assert mk_dictionary_12(1, 2) == {"data": {1: 2}}
    assert mk_dictionary_12(
        1, True, (1, 2, 3), {3: 3}, "qwe", 7.8
    ) == {  # noqa: JS101
        "data": {1: True, (1, 2, 3): {3: 3}, "qwe": 7.8}
    }
    assert mk_dictionary_12(1, [1, 2, 34]) == {"error": "Invalid type"}
