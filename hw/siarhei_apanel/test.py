from hw.siarhei_apanel.refakt import korteg
from hw.siarhei_apanel.refakt import krypto
from hw.siarhei_apanel.refakt import newwords
from hw.siarhei_apanel.refakt import srez
from hw.siarhei_apanel.refakt import stroki
from hw.siarhei_apanel.refakt import zaglav


def test_example() -> None:  # noqa: W503
    cod = "VD DzgS PwFl DzgS SDK ZFz HD"
    key = "FTZHfrcwtoRgQzDaspdlKiPvSYLekVCqhJbyEnmMBAOIxuXjWUNG"  # noqa: E501
    assert korteg([1, 3.0, "re", 8]) == (1, 8)
    assert newwords("asfN dB12") == "dB12 asfN"
    assert srez([2, 14, "b", "h"], "r") == [2, 14, "b", "h", "r"]
    assert stroki("a4N67;i", "V") == "aV4VNV6V7V;Vi"
    assert zaglav("HI nub  hI   PrO") == "Hi Nub  Hi   Pro"
    assert (
        krypto(cod, key) == "Do only what only you can do"  # noqa: W503, E501
    )  # noqa: W503, E501
