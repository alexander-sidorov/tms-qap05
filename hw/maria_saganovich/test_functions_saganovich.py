from hw.maria_saganovich.functions_hw import func1
from hw.maria_saganovich.functions_hw import func2
from hw.maria_saganovich.functions_hw import func3
from hw.maria_saganovich.functions_hw import func4
from hw.maria_saganovich.functions_hw import func_5


def test_functions() -> None:
    assert func1() is False
    assert func2() is True
    assert func3() is None  # type: ignore
    assert func4() == -100
    assert func_5() == ""
