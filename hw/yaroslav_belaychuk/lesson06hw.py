def cortage(a1: list) -> tuple:
    return a1[0], a1[-1]


def string(b1: str) -> str:
    b1 = b1.split()
    b1 = b1[::-1]
    b1 = b1[0] + " " + b1[1]
    return b1


def collection(c1: list, c2: any) -> list:  # type:  ignore
    c1.append(c2)
    return c1


def str_in_str(d1: str, d2: str) -> str:
    string = d2.join(d1)
    return string


def string_zaglavie(q1: str) -> str:
    return q1.title()