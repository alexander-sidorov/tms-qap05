from refakt import func


def test() -> None:
    assert func(1, 2, 1) == [-1.0, -1.0]
    assert func(1, 1, 1) == [
        (-0.49999999999999994 + 0.8660254037844386j),
        (-0.5 - 0.8660254037844386j),
    ]
