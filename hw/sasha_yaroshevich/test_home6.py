from hw.sasha_yaroshevich.home_work6 import polindrom


def test_home6_polindrom() -> bool:
    polindrom_inp = "xyx"
    assert polindrom(polindrom_inp) == {"data": True}
