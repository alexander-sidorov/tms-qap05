from hw.sasha_yaroshevich.home_work6 import polindrom_1
from hw.sasha_yaroshevich.home_work6 import proizvedenie_2
from hw.sasha_yaroshevich.home_work6 import date_rojdeniya


def test_home6() -> None:
    polindrom_inp = "xyx"
    assert polindrom_1(polindrom_inp) == {"data": True}
    assert proizvedenie_2(1,2) == {"data": 2}
    assert proizvedenie_2(0, 1, 2, 3) == {"data": 0}
    assert proizvedenie_2(1, "2", 3) == {"data": "222"}
    assert date_rojdeniya(1993, 3, 20) == {"data": {"year": 1993, "month": 3, "day": 20, "age": 29}}

