from hw.siarhei_apanel.refakt import aggression
from hw.siarhei_apanel.refakt import far
from hw.siarhei_apanel.refakt import func
from hw.siarhei_apanel.refakt import gar
from hw.siarhei_apanel.refakt import korteg
from hw.siarhei_apanel.refakt import krypto
from hw.siarhei_apanel.refakt import newwords
from hw.siarhei_apanel.refakt import srez
from hw.siarhei_apanel.refakt import stroki
from hw.siarhei_apanel.refakt import zaglav


def test_example() -> None:  # noqa: W503
    co = "VD DzgS PwFl DzgS SDK ZFz HD"
    ke = "FTZHfrcwtoRgQzDaspdlKiPvSYLekVCqhJbyEnmMBAOIxuXjWUNG"  # noqa: E501
    assert korteg([1, 3.0, "re", 8]) == (1, 8)
    assert korteg([1]) == (1, 1)
    assert korteg([]) == ()
    assert newwords("asfN dB12") == "dB12 asfN"
    assert newwords("asfNdB12") == "asfNdB12"
    assert srez([2, 14, "b", "h"], "r") == [2, 14, "b", "h", "r"]
    assert stroki("a4N67;i", "V") == "aV4VNV6V7V;Vi"
    assert stroki("a4N67;i", "") == "a4N67;i"
    assert zaglav("") == ""
    assert krypto(co, ke) == "Do only what only you can do"  # noqa: W503, E501
    assert far() is None  # type: ignore
    assert gar() == 4
    assert aggression(True) == "Оно и видно!"
    assert aggression(False) == "А могли бы и знать!"
    assert func(1, 2, 1) == [-1.0, -1.0]
    assert func(1, 1, 1) == [
        (-0.49999999999999994 + 0.8660254037844386j),
        (-0.5 - 0.8660254037844386j),
    ]
