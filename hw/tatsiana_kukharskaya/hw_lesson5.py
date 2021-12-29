def just_do_it1(me: list) -> tuple:
    return (me[0], me[-1])


def just_do_iit1(me: list) -> tuple:
    working = operator.itemgetter(0, -1)
    f = working(me)
    return tuple(f)


def just_do_it2(wichtig: str) -> str:
    just_for_u = wichtig.rsplit()
    return f"{just_fo_u[1]} {just_fo_u[0]}"


def just_do_it3(nejki: list, nejki2: str) -> list:
    nechto = nejki.index(nejki2)
    return nejki[0 : nechto +1]


def just_do_it4(string_1: str, string_2: str) -> str:
    string_neu = list(string_1)
    string_pl = string_2.join(string_neu)
    return string_pl + string_2


def just_do_it5(string: str) -> str:
    return string.title()
