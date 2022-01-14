from datetime import date

from hw.maria_saganovich.lesson6_hw.lvl4_oldest import func4_oldest


def test_func4_oldest() -> None:
    d0 = [date(2000, 6, 8), date(1999, 6, 8)]
    d1 = {"A": date(2000, 6, 8), "B": date(1999, 6, 8)}
    d2 = {"A": date(2000, 6, 8), "B": date(1999, 6, 8), "C": date(1998, 6, 8)}
    d3 = {"A": date(2000, 6, 8), "B": date(1999, 6, 8), "C": "1998, 6, 8"}
    d4 = {"A": date(2023, 6, 8), "B": date(2024, 6, 8), "C": date(1998, 6, 8)}
    d5 = {"A": date(2000, 6, 8), "B": date(2024, 6, 8), "C": "1998, 6, 8"}
    d6 = {"A": date(2000, 6, 8), "B": "1998, 6, 8", "C": date(2024, 6, 8)}
    d7 = {"Jasmin": date(1998, 6, 8), "Aria": date(1998, 6, 8)}
    assert func4_oldest(d0) == {"errors": ["should be dict"]}
    assert func4_oldest(d1) == {"data": "B"}
    assert func4_oldest(d2) == {"data": "C"}
    assert func4_oldest(d3) == {"errors": ["args should be date"]}
    assert func4_oldest(d4) == {"errors": ["is not born"]}
    assert func4_oldest(d5) == {"errors": ["is not born"]}
    assert func4_oldest(d6) == {"errors": ["args should be date"]}
    assert func4_oldest(d7) == {"data": "Jasmin"}
