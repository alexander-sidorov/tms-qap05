def func4(some_string: str, some_string2: str) -> str:
    ss1 = [char for char in some_string]  # noqa: C416
    return some_string2.join(ss1)
