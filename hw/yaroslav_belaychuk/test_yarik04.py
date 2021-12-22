from hw.yaroslav_belaychuk.test_yarikhw import fnc


def test_f() -> None:
    assert fnc(1, 4, 9) == [(-4 + 2.23606797749979j), (-4 - 2.23606797749979j)]
    assert fnc(1, 1, 1) == [
        (-1 + 0.8660254037844386j),
        (-1 - 0.8660254037844386j),
    ]
    assert fnc(1, 2, 1) == [-2.0, -2.0]
