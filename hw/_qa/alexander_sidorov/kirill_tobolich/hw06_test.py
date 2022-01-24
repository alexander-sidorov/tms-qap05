from secrets import choice
from string import ascii_letters
from typing import Any
from typing import Callable

import pytest

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


class UndefinedType:
    pass


Undefined = UndefinedType()


def lol() -> Any:
    name = "".join(choice(ascii_letters) for _ in range(24))
    typ = type(name, (), {})
    return typ()


def validate(
    func: Callable,
    *args: Any,
    xdata: Any = Undefined,
    xerrors: bool = False,
) -> None:
    result = func(*args)

    if xerrors:
        errors = result.get("errors")
        assert errors
        assert isinstance(errors, list)
        for error in errors:
            assert isinstance(error, str)
        assert errors == sorted(errors)
        return

    if xdata is not Undefined:
        data = result.get("data", Undefined)
        assert data is not Undefined
        assert data == xdata
        return

    raise AssertionError("invalid usage of validate()")


def test_xxx() -> None:
    with pytest.raises(AssertionError):
        validate(palindrome, "")
    with pytest.raises(AssertionError):
        validate(palindrome, "", xdata=Undefined)


def test_task_01() -> None:
    validate(palindrome, "", xdata=True)
    validate(palindrome, lol(), xerrors=True)


def test_task_02() -> None:
    validate(multiply, xerrors=True)
    validate(multiply, "a", 2, "a", xerrors=True)


def test_task_03() -> None:
    validate(get_formatted_birthday, lol(), xerrors=True)


def test_task_04() -> None:
    validate(get_the_eldest, lol(), xerrors=True)
    validate(get_the_eldest, {1: lol()}, xerrors=True)


def test_task_05() -> None:
    validate(
        get_the_same_elements_in_collection,
        {1, 2, 3, 4, 5},
        xdata={},
    )

    validate(
        get_the_same_elements_in_collection,
        {1: 1, 2: 1, 3: 1, 4: 1, 5: 1},
        xdata={},
    )

    validate(
        get_the_same_elements_in_collection,
        lol(),
        xerrors=True,
    )

    validate(
        get_the_same_elements_in_collection,
        [[], {}],
        xerrors=True,
    )


def test_task_06() -> None:
    validate(
        http_query_parser,
        "xx=",
        xdata={"xx": [""]},
    )
    validate(
        http_query_parser,
        "xx=&yy=",
        xdata={"xx": [""], "yy": [""]},
    )
    validate(
        http_query_parser,
        "xx=12&yy=34&yy=56",
        xdata={"xx": ["12"], "yy": ["34", "56"]},
    )

    validate(
        http_query_parser,
        lol(),
        xerrors=True,
    )


def test_task_07() -> None:
    validate(
        repeat_chars,
        lol(),
        xerrors=True,
    )


def test_task_08() -> None:
    validate(
        count_chars,
        "",
        xdata="",
    )
    validate(
        count_chars,
        "a",
        xdata="a1",
    )
    validate(
        count_chars,
        "ab",
        xdata="a1b1",
    )
    validate(
        count_chars,
        "aba",
        xdata="a1b1a1",
    )

    validate(
        count_chars,
        lol(),
        xerrors=True,
    )


def test_task_09() -> None:
    validate(
        inverted_dictionary,
        lol(),
        xerrors=True,
    )
    validate(
        inverted_dictionary,
        {1: []},
        xerrors=True,
    )


def test_task_10() -> None:
    validate(
        zip_collections_to_dict,
        lol(),
        lol(),
        xerrors=True,
    )

    validate(
        zip_collections_to_dict,
        [[]],
        [{}],
        xerrors=True,
    )


def test_task_11() -> None:
    validate(
        relations_between_two_sets,
        lol(),
        lol(),
        xerrors=True,
    )


def test_task_12() -> None:
    validate(
        make_dictionary,
        xdata={},
    )

    validate(
        make_dictionary,
        1,
        xerrors=True,
    )
    validate(
        make_dictionary,
        [],
        1,
        xerrors=True,
    )
