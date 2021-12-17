def f() -> None:
	5

def test_f() -> None:
	assert f() is None #type: ignore
