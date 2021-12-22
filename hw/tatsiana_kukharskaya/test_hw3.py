from hw.tatsiana_kukharskaya.hw3 import avr1, avr2, kim, k, den


def alle() -> None:
    assert avr1() is True
    assert avr2() is False
    assert kim() < 0
    assert k() is None  # type: ignore
    assert den() == ""
