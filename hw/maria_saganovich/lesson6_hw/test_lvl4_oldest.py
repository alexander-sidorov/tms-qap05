from datetime import date
from datetime import datetime

from hw.maria_saganovich.lesson6_hw.lvl4_oldest import func4_oldest


def test_func4_oldest() -> None:
    d0 = {"A": date(2000, 6, 8), "B": date(1999, 6, 8)}
    d1 = {"A": date(2000, 6, 8), "B": date(1999, 6, 8), "C": date(1998, 6, 8)}
    d2 = {"Jasmin": date(1998, 6, 8), "Aria": date(1998, 6, 8)}
    aria_bd = datetime.now().replace(year=1990, month=1, day=1)
    d3 = {"A": date(2000, 6, 8), "B": aria_bd}
    assert func4_oldest(d0) == {"data": "B"}
    assert func4_oldest(d1) == {"data": "C"}
    assert func4_oldest(d2) == {"data": "Jasmin"}
    assert func4_oldest(d3) == {"data": "B"}
