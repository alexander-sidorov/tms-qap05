from typing import Any

col01 = [1, 2, 3, 4, 5, 6, 7]
col02 = "tuda suda"


def first_last_elements(collection: col01) -> tuple:
    return (min(col01)), (max(col01))


def swapped_words(collection: col02) -> str:
    return f"{col02[-4:]} {col02[:4]}"


def slice_of_col03(collection: Any, some_object: Any) -> Any:
    index = collection.index(some_object)
    return collection[: index + 1]


def string_combination(string01: str, string02: str) -> str:
    return string01.join(string02)


def titled_string(some_string: str) -> str:
    return some_string.title()
