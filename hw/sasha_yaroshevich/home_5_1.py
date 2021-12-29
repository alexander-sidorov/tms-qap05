from typing import Any


def funct(sort_collection: Any) -> tuple:
    return (sort_collection[0], sort_collection[-1])


def func(stroka_two_words: str) -> str:
    new_a = stroka_two_words.split(" ")
    new_b = [new_a[-1], new_a[0]]
    return " ".join(new_b)


def fun(sort_coll: Any, p2: int) -> Any:
    limit = sort_coll.index(p2)
    return sort_coll[0 : limit + 1]  # noqa: E203


def fu(stroka: str, stroka_one: str) -> str:
    new_stroka = list(stroka)
    stroka_s = stroka_one.join(new_stroka)
    return stroka_s


def f(stroka_pr: str) -> str:
    return stroka_pr.title()
