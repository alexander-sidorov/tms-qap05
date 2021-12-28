from hw.denis_asipenko.func_hw5 import task_1
from hw.denis_asipenko.func_hw5 import task_2
from hw.denis_asipenko.func_hw5 import task_3
from hw.denis_asipenko.func_hw5 import task_4
from hw.denis_asipenko.func_hw5 import task_5


def test_myhw5() -> None:
    test_list = [5, 8, 13, 26, 83]
    test_words = "Denis Asipenko"
    test_object = 26
    test_symbol = "s"
    test_text = "KEEP calm and code python."  # noqa: E501
    assert task_1(test_list) == (5, 83)
    assert task_2(test_words) == "Asipenko Denis"
    assert task_3(test_list, test_object) == [5, 8, 13, 26]
    assert (
        task_4(test_symbol, test_text)
        == "KsEsEsPs scsaslsms sasnsds scsosdses spsystshsosns."
    )
    assert task_5(test_text) == "Keep Calm And Code Python."  # noqa: E501,W503
