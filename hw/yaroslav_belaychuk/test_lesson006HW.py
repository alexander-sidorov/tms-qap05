from datetime import date

from hw.yaroslav_belaychuk.lesson006HW import date_age
from hw.yaroslav_belaychuk.lesson006HW import palindrom
from hw.yaroslav_belaychuk.lesson006HW import umnogenie
from hw.yaroslav_belaychuk.lesson006HW import zadacha_4
from hw.yaroslav_belaychuk.lesson006HW import zadacha_5
from hw.yaroslav_belaychuk.lesson006HW import zadacha_7


def test_function() -> None:
    d1 = date(year=1987, month=8, day=2)
    d2 = (1987, 8, 2)
    f1 = {"nik": date(1988, 8, 2), "vika": date(1953, 5, 9)}
    assert palindrom("") == {"data": True}
    assert palindrom("x") == {"data": True}
    assert palindrom("xx") == {"data": True}
    assert palindrom("xy") == {"data": False}
    assert palindrom(1) == {"errors": ["TypeErrors"]}   # type: ignore
    assert umnogenie(1, 2, 3) == {"data": 6}
    assert umnogenie(1) == {"data": 1}
    assert umnogenie(1, 2) == {"data": 2}
    assert umnogenie("1", 3) == {"data": "111"}
    assert date_age(d1) == {
        "data": {"year": 1987, "month": 8, "day": 2, "age": 34}
    }
    assert date_age(d2) == {"TypeError"}   # type: ignore
    assert zadacha_4(f1) == {"data": "vika"}
    assert zadacha_5(("a", "a", 1, 2)) == {"data": {"a": 2}}
    assert zadacha_5({(), "", "", 1}) == {"errors": ["NoRepeatError"]}
    assert zadacha_7("a3b4c2") == {"data": "aaabbbbcc"}
    assert zadacha_7("a3b2c") == {"Error"}
    assert zadacha_7(["a3b4c5"]) == {"TypeError"}   # type: ignore
