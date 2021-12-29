from typing import Any


def first_last_elements(collection: Any) -> tuple:
    return collection[0], collection[-1]


def swapped_words(string: str) -> str:
    col02 = string.rsplit()
    return f"{col02[1]} {col02[0]}"


def slice_of_col03(collection: Any, some_object: Any) -> Any:
    index = collection.index(some_object)
    return collection[: index + 1]


def string_combination(string01: str, string02: str) -> str:
    return string02.join(string01)


def titled_string(some_string: str) -> str:
    return some_string.title()
