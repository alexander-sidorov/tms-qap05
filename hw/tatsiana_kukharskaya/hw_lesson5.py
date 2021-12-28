import operator


def just_do_it1(me: list) -> tuple:
    working = operator.itemgetter(0, -1)
    f = working(me)
    return tuple(f)


def just_do_it2(wichtig: str) -> str:
    just_for_u = wichtig.rsplit()
    return f"{just_fo_u[1]} {just_fo_u[0]}"


def just_do_it3(nejki: list, nejki2: str) -> list:

    nechto1 = nechto(None, nejki.index(nejki2) + 1)
    return nejki[nechto1]


def just_do_it4(string_1: str, string_2: str) -> str:
    string_res = ""
    for a in string_1:
        string_res += a
        string_res += string_2
    return string_res


def just_do_it5(string: str) -> str:
    return string.title()