from hw.sasha_yaroshevich.home_5_1 import f
from hw.sasha_yaroshevich.home_5_1 import fu
from hw.sasha_yaroshevich.home_5_1 import fun
from hw.sasha_yaroshevich.home_5_1 import func
from hw.sasha_yaroshevich.home_5_1 import funct


def test_home_5_1() -> None:
    funct_coll = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    func_stroka = "Hello world"
    fun_1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    fun_2 = 5
    fu_1 = "abcdef"
    fu_2 = "2"
    f_last = "abc vbd   fdsg wrwr"
    assert funct(funct_coll) == [1, 10]
    assert func(func_stroka) == "worldHello"
    assert fun(fun_1, fun_2) == [1, 2, 3, 4, 5]
    assert fu(fu_1, fu_2) == "a2b2c2d2e2f2"
    assert f(f_last) == "Abc Vbd   Fdsg Wrwr"
