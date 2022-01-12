from datetime import date

from hw.vlad_yancharski.hw6.func_6 import age
from hw.vlad_yancharski.hw6.func_6 import factorial
from hw.vlad_yancharski.hw6.func_6 import older
from hw.vlad_yancharski.hw6.func_6 import palindrom


def test_task01() -> None:
    assert palindrom("a   a a") == {"data": False}
    assert palindrom("a a a") == {"data": True}
    assert palindrom("1 2 33 2  1") == {"data": False}


def test_task02() -> None:
    assert factorial(1, 2, 3) == {"data": 6}
    assert factorial(3, 5, 10) == {"data": 150}


def test_task03() -> None:
    d = date(year=1987, month=8, day=2)
    assert age(d) == {"data": {"year": 1987, "month": 8, "day": 2, "age": 34}}
    b = date(year=2003, month=7, day=29)
    assert age(b) == {"data": {"year": 2003, "month": 7, "day": 29, "age": 18}}


def test_task04() -> None:
    d = {
        "A": date(year=2000, month=5, day=15),
        "B": date(year=1999, month=9, day=21),
    }
    assert older(d) == {"data": "B"}
    b = {
        "Kate": date(year=1988, month=2, day=2),
        "Paul": date(year=2021, month=4, day=29),
        "Vlad": date(year=2003, month=8, day=12),
        "Mike": date(year=1976, month=11, day=8),
    }
    assert older(b) == {"data": "Mike"}
