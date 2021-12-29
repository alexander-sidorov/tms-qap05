from hw.tatsiana_kukharskaya.hw_lesson5 import just_do_it1
from hw.tatsiana_kukharskaya.hw_lesson5 import just_do_iit1
from hw.tatsiana_kukharskaya.hw_lesson5 import just_do_it2
from hw.tatsiana_kukharskaya.hw_lesson5 import just_do_it3
from hw.tatsiana_kukharskaya.hw_lesson5 import just_do_it4
from hw.tatsiana_kukharskaya.hw_lesson5 import just_do_it5


def just_do_it() -> None:
    me = ["Help", "Me", "Please"]
    just_for_test = "true It's"
    nechto3 = ["It's", "so", "wonderfull", "for", "me"]
    nejki2 = nechto3[2]
    string_for_test = "Tatsin Vsses"
    char_for_test = "a"
    for_test = "Do YoU like apple ?"  # noqa: E501
    assert just_do_it1(me) == ("Help", "Please")
    assert just_do_iit1(me) == ("Help", "Please")
    assert just_do_it2(just_for_test) == "It's true"
    assert just_do_it3(nechto3, nejki2) == ["It's", "so", "wonderfull"]
    assert (
        just_do_it4(string_for_test, char_for_test)
        == "Taatasaiana Vasasaeasa"  # noqa: W503
    )
    assert just_do_it5(for_test) == "Do You Like Apple ?"  # noqa: E501,W503
