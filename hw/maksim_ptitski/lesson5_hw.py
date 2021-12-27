from typing import Any


def first_and_last_collection_element(collection: Any) -> tuple:
    return collection[0], collection[-1]


def two_words_reversed(string: str) -> str:
    i = string.index(" ")
    first_word = string[:i]
    second_word = string[i + 1 :]  # noqa: E203
    return f"{second_word} {first_word}"


def combine_result(collection: Any, object_1: Any) -> Any:
    i = collection.index(object_1)
    return collection[: i + 1]


def separated_string(string_1: str, string_2: str) -> str:
    string_result = ""
    for i in string_1:
        string_result += i
        string_result += string_2
    return string_result


def string_with_capitalized_letters(string: str) -> str:
    return string.title()
