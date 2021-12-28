from typing import Any


def first_last_elements(collection: Any) -> tuple:
    return (min(collection)), (max(collection))


def swapped_words(string: str) -> str:
    col02 = string
    return f"{col02[-4:]} {col02[:4]}"


def slice_of_col03(collection: Any, some_object: Any) -> Any:
    index = collection.index(some_object)
    return collection[: index + 1]


def string_combination(string01: str, string02: str) -> str:
    return string01.join(string02)


def titled_string(some_string: str) -> str:
    return some_string.title()
