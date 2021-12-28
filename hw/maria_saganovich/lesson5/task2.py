def func2(some_string: str) -> str:
    string_spl = some_string.split(" ")
    return " ".join([string_spl[1], string_spl[0]])
