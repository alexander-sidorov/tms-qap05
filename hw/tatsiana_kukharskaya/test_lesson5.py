import operator


def just_do_it1(me: list) -> tuple:
    working = operator.itemgetter(0, -1)
    f = working(me)
    return tuple(f)

def just_do_it1() -> None:
    me = ["Help", "Me", "Please"]
    assert just_do_it1(me) == ("Help", "Please")



def just_do_it2(wichtig: str) -> str:
    just_for_u = wichtig.rsplit()
    return f"{just_fo_u[1]} {just_fo_u[0]}"

def just_do_it2() -> None:
     just = "true It's"
     assert just_do_it2(just) == "It's true"


def just_do_it3(nejki: list, nejki2: str) -> list:

    nechto1 = nechto(None, nejki.index(nejki2) + 1)
    return nejki[nechto1]

def just_do_it3() -> None:
    nechto3 = ["It's", "so", "wonderfull", "for", "me"]
    nejki2 = nechto3[2]
    assert just_do_it3(nechto3, nejki2) == ["It's", "so", "wonderfull"]


def just_do_it4(string_1: str, string_2: str) -> str:
    string_res = ""
    for a in string_1:
        string_res += a
        string_res += string_2
    return string_res

def just_do_it4() -> None:
    string_for_test = "Tatsin Vsses"
    char_for_test = a
    assert (
            just_do_it4(string_for_test, char_for_test)
            == "Taatasaiana Vasasaeasa"  # noqa: W503
    )


def just_do_it5(string: str) -> str:
    return string.title()

def just_do_it5() -> None:
    for_test = "Do YoU like apple ?"  # noqa: E501
    assert (
        just_do_it5(for_test)
        == "Do You Like Apple ?"  # noqa: E501,W503
    )