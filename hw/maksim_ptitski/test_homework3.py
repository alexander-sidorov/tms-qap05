from hw.maksim_ptitski.lesson3 import func1
from hw.maksim_ptitski.lesson3 import func2
from hw.maksim_ptitski.lesson3 import func3
from hw.maksim_ptitski.lesson3 import func4
from hw.maksim_ptitski.lesson3 import func5


def test_function() -> None:
    assert func1() is True
    assert func2() is False
    assert func3() is None  # type: ignore
    assert func4() < 0
    assert func5() == ""
