def aggression(know: bool) -> str:
    if know:
        return "но и видно"
    else:
        return " мог бы и знать"


def test_f() -> None:
    assert aggression(True) == "но и видно"
    assert aggression(False) == " мог бы и знать"


if __name__ == "__main__":
    aggression(True)
