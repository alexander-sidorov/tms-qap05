from hw.vadim_maletski.func5 import level1
from hw.vadim_maletski.func5 import level2
from hw.vadim_maletski.func5 import level3
from hw.vadim_maletski.func5 import level4
from hw.vadim_maletski.func5 import level5
from hw.vadim_maletski.func5 import level6


def test() -> None:

    assert level1([4, 6, 7, 8.5, "Hello"]) == (4, "Hello")
    assert level2("Hello Python") == "Python Hello"
    assert level3([True, 4, 6, 7, 8.5, "Hello"]) == [True, 4, 6, 7]
    assert level4("68 Hello 4 8 9 2") == "6W8W WHWeWlWlWoW W4W W8W W9W W2W"
    assert level5("heLLo mY   python  vEr 3.10") == "Hello My Python Ver 3.10"
    assert (
        level6(
            "VD DzgS PwFl DzgS SDK ZFz HD",
            "FTZHfrcwtoRgQzDaspdlKiPvSYLekVCqhJbyEnmMBAOIxuXjWUNG ",
            "ABCDIFGHEJKLMNOPQRSTUVWXYZABCDIFGHEJKLMNOPQRSTUVWXYZ ",
        )
        == "DO ONLY WHAT ONLY YOU CAN DO"  # noqa: W503
    )
