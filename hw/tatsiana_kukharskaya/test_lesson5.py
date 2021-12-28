from hw.tatsiana_kukharskaya.hw_lesson5 import just_do_it1


def just_do_it1() -> None:
    me = ["Help", "Me", "Please"]
    assert just_do_it1(me) == ("Help", "Please")


from hw.tatsiana_kukharskaya.hw_lesson5 import just_do_it2


def just_do_it2() -> None:
    just_for_test = "true It's"
    assert just_do_it2(just_for_test) == "It's true"


from hw.tatsiana_kukharskaya.hw_lesson5 import just_do_it3


def just_do_it3() -> None:
    nechto3 = ["It's", "so", "wonderfull", "for", "me"]
    nejki2 = nechto3[2]
    assert just_do_it3(nechto3, nejki2) == ["It's", "so", "wonderfull"]


from hw.tatsiana_kukharskaya.hw_lesson5 import just_do_it4


def just_do_it4() -> None:
    string_for_test = "Tatsin Vsses"
    char_for_test = "a"
    assert (
        just_do_it4(string_for_test, char_for_test)
        == "Taatasaiana Vasasaeasa"  # noqa: W503
    )


from hw.tatsiana_kukharskaya.hw_lesson5 import just_do_it5


def just_do_it5() -> None:
    for_test = "Do YoU like apple ?"  # noqa: E501
    assert just_do_it5(for_test) == "Do You Like Apple ?"  # noqa: E501,W503
