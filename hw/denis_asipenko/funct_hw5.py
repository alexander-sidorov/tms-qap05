from typing import Any


def task_1(collection: Any) -> tuple:
    return collection[0], collection[-1]


def task_2(string: str) -> str:
    test_words = string.rsplit()
    return f"{test_words[1]} {test_words[0]}"


def task_3(collection: Any, test_object: Any) -> Any:
    index = collection.index(test_object)
    return collection[: index + 1]


def task_4(test_symbol: str, test_text: str) -> str:
    return test_symbol.join(test_text)


def task_5(test_text: str) -> str:
    return test_text.title()
