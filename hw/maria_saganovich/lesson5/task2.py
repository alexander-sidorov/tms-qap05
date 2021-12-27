def func2(some_string: str) -> str:
    string_spl = some_string.split(" ")
    my_order = [1, 0]
    return " ".join([string_spl[i] for i in my_order])
