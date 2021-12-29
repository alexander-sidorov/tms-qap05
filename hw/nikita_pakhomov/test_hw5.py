from hw.nikita_pakhomov.nlesson3.lesoon5hw import lwl1
from hw.nikita_pakhomov.nlesson3.lesoon5hw import lwl3
from hw.nikita_pakhomov.nlesson3.lesoon5hw import lwl5
from hw.nikita_pakhomov.nlesson3.lesoon5hw import strok


def test_strok() -> None:
    assert strok("111 222") == "222 111"


def test_lwl1() -> None:
    assert lwl1((1, 2, 3, 4)) == (1, 4)


def test_lwl3() -> None:
    assert lwl3(([1, 2, 3, 4, 5]), 2) == [1, 2]
    assert lwl3("abcdef", "d") == "abcd"
    assert lwl3(("x", "y", "z"), "y") == ("x", "y")


def test_lwl5() -> None:
    assert lwl5("xxx xxx") == "Xxx Xxx"
