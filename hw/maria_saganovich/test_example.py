from hw.maria_saganovich.functions_examle import func2
from hw.maria_saganovich.functions_examle import func_1
from hw.maria_saganovich.functions_examle import func_4


def test_example() -> None:
    assert True, "not True"
    assert func_4() == 102
    assert func_1() != 1
    assert func2() == "South Korea"
