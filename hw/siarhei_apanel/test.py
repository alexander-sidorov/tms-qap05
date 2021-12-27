from hw.siarhei_apanel.refakt import korteg
from hw.siarhei_apanel.refakt import krypto
from hw.siarhei_apanel.refakt import newwords
from hw.siarhei_apanel.refakt import srez
from hw.siarhei_apanel.refakt import stroki
from hw.siarhei_apanel.refakt import zaglav


def test_example() -> None:
    cod = "VD DzgS PwFl DzgS SDK ZFz HD"
    key = "FTZHfrcwtoRgQzDaspdlKiPvSYLekVCqhJbyEnmMBAOIxuXjWUNG"
    assert korteg([1, 3, 5, 8]) == (1, 8)
    assert newwords("asfN dB12") == "dB12 asfN"
    assert srez([2, 14, "b", "h", "e"], "r") == [2, 14, "b", "h", "e", "r"]
    assert stroki("a4N67;i", "V") == "aV4VNV6V7V;ViV"
    assert zaglav("HI nub  hI   PrO") == "Hi Nub  Hi   Pro"
    assert (
        krypto(cod, key)
        == "D o   o n l y   w h a t   o n l y   y o u   c a n   d o"
    )  # noqa: W503
