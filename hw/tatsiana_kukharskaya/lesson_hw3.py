def avr1() -> bool:
    k = 21
    p = 3
    a = k / p
    return a 


def avr2() -> bool:
    i = 0
    return i


def kim() -> int:
    p = -8
    return p


def k() -> None:
    x = 3
    y = x
    r = y - x
    return r


def den() -> str:
    return ""


def alle() -> None:
    assert avr1() is True
    assert avr2() is False
    assert kim() < 0
    assert k() is None
    assert den() == ""
