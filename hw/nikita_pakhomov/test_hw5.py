from hw.nikita_pakhomov.nlesson3.lesoon5hw import strok


def test_strok() -> None:
    assert strok("111 222") == "222 111"


if __name__ == "__main__":
    strok("111 222")
