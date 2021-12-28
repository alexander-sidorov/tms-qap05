from hw.nikita_pakhomov.nlesson3.lesoon5hw import lwl1
from hw.nikita_pakhomov.nlesson3.lesoon5hw import strok


def test_strok() -> None:
    assert strok("111 222") == "222 111"


if __name__ == "__main__":
    strok("111 222")


def test_lwl1() -> None:
    assert lwl1((1, 2, 3, 4)) == (1, 4)


if __name__ == "__main__":
    lwl1((1, 4))
