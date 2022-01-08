from hw.maria_saganovich.lesson6_hw.lvl3_age import func3_age
from datetime import date


def test_func3_age() -> None:
    date1 = date(1987, 8, 2)
    date2 = date(1992, 2, 29)
    date3 = "2001-01-02"
    d4 = date.today()
    assert func3_age(date1) == {"data": {"year": 1987, "month": 8, "day": 2, "age": 34}}
    assert func3_age(date2) == {"data": {"year": 1992, "month": 2, "day": 29, "age": 29}}
    assert func3_age(date3) == {"errors": ["should be date"]}
    assert func3_age(d4) == {"data": {"year": d4.year, "month": d4.month, "day": d4.day, "age": 0}}
