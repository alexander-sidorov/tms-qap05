def func4(some_string: str, some_string2: str) -> str:
    result: str = ""
    for char in some_string:
        result += char + some_string2
    return result
