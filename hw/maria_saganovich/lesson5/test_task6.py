from hw.maria_saganovich.lesson5.task6 import func6
from hw.maria_saganovich.lesson5.task6 import func_encryption


def test_func6() -> None:
    msg1 = "Santa Claus is coming to town"
    params = func_encryption(msg1)
    assert func6(params[0], params[1]) == "Santa Claus is coming to town"
