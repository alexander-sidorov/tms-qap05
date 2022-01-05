from hw.sasha_yaroshevich.home_work6 import polindrom_1
from hw.sasha_yaroshevich.home_work6 import proizvedenie_2


def test_home6() -> None:
    polindrom_inp = "xyx"
    proizvedenie_dan = (1, 2)
    assert polindrom_1(polindrom_inp) == {"data": True}
    assert proizvedenie_2(proizvedenie_dan) == {"data": 2}

