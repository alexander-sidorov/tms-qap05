from hw.siarhei_apanel.refakt import aggression


def test() -> None:
    assert aggression(True) == "Оно и видно!"
    assert aggression(False) == "А могли бы и знать!"
