def avr1() -> bool:
    return True 


def avr2() -> bool:
    return False


def kim() -> int:
    return -8


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
