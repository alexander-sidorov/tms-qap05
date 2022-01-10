from datetime import date

from hw._qa.alexander_sidorov.common import validate
from hw._qa.alexander_sidorov.common import xoxo
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


def test_task_01() -> None:
    validate(
        if_palindrome_1,
        xoxo(),
        expected_errors=[],
    )

    validate(if_palindrome_1, "", expected_data=True)
    validate(if_palindrome_1, "a   a a", expected_data=False)
    validate(if_palindrome_1, "a", expected_data=True)
    validate(if_palindrome_1, "Aa", expected_data=False)
    validate(if_palindrome_1, "aa", expected_data=True)
    validate(if_palindrome_1, "⚠️⚠️", expected_data=False)


def test_task_02() -> None:
    validate(
        multiplication_2,
        {},
        expected_errors=[],
    )

    validate(
        multiplication_2,
        {},
        set(),
        expected_errors=[],
    )

    validate(
        multiplication_2,
        2,
        "a",
        2,
        "a",
        expected_errors=[],
    )

    validate(multiplication_2, 1, expected_data=1)
    validate(multiplication_2, 1, 2, 3, expected_data=6)
    validate(multiplication_2, [1], 2, expected_data=[1, 1])
    validate(multiplication_2, 2, [1], 2, expected_data=[1, 1, 1, 1])
    validate(multiplication_2, 2, "a", 2, expected_data="aaaa")
    validate(multiplication_2, 2, "a", expected_data="aa")
    validate(multiplication_2, "a", 2, expected_data="aa")


def test_task_03() -> None:
    validate(
        birthday_3,
        xoxo(),
        expected_errors=[],
    )

    validate(
        birthday_3,
        date(date.today().year + 1, 1, 1),
        expected_errors=[],
    )


def test_task_04() -> None:
    validate(
        oldest_4,
        xoxo(),
        expected_errors=[],
    )

    validate(
        oldest_4,
        {1: xoxo()},
        expected_errors=[],
    )

    validate(
        oldest_4,
        {None: date(2990, 1, 1), ...: date(2000, 1, 1)},
        expected_data=...,
    )


def test_task_05() -> None:
    validate(
        duplicates_5,
        {},
        expected_data={},
    )

    validate(
        duplicates_5,
        [{}, set()],
        expected_data={},
    )


def test_task_06() -> None:
    validate(
        dict_from_http_6,
        xoxo(),
        expected_errors=[],
    )


def test_task_07() -> None:
    validate(
        repeated_symbols_7,
        xoxo(),
        expected_errors=[],
    )

    validate(
        repeated_symbols_7,
        "a",
        expected_errors=[],
    )

    validate(
        repeated_symbols_7,
        "1a",
        expected_errors=[],
    )

    validate(
        repeated_symbols_7,
        "aaa11",
        expected_errors=[],
    )

    validate(
        repeated_symbols_7,
        "",
        expected_data="",
    )

    validate(
        repeated_symbols_7,
        "a2b2a1",
        expected_data="aabba",
    )

    validate(
        repeated_symbols_7,
        "a11b1",
        expected_data="aaaaaaaaaaab",
    )


def test_task_08() -> None:
    validate(
        count_amount_8,
        xoxo(),
        expected_errors=[],
    )

    validate(
        count_amount_8,
        "aba",
        expected_data="a1b1a1",
    )


def test_task_09() -> None:
    validate(
        revert_dictionary_9,
        xoxo(),
        expected_errors=[],
    )

    validate(
        revert_dictionary_9,
        {1: [], 2: set(), 3: {}},
        expected_errors=[],
    )


def test_task_10() -> None:
    keks = [{}, {1}, ..., None, False, True, 1, 1j, 1.0j, xoxo()]
    for kek1 in keks:
        for kek2 in keks:
            validate(
                join_dictionary_10,
                kek1,
                kek2,
                expected_errors=[],
            )


def test_task_11() -> None:
    validate(
        set_operations_11,
        xoxo(),
        xoxo(),
        expected_errors=[],
    )


def test_task_12() -> None:
    validate(
        mk_dictionary_12,
        xoxo(),
        expected_errors=[],
    )

    validate(
        mk_dictionary_12,
        [],
        1,
        expected_errors=[],
    )

    validate(
        mk_dictionary_12,
        {},
        1,
        expected_errors=[],
    )

    validate(
        mk_dictionary_12,
        set(),
        1,
        expected_errors=[],
    )
