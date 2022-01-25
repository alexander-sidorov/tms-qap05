import collections
from datetime import date
from typing import Any
from typing import Collection

from hw.kirill_tobolich.lesson6_hw import get_formatted_birthday
from hw.kirill_tobolich.lesson6_hw import http_query_parser
from hw.kirill_tobolich.lesson6_hw import multiply
from hw.kirill_tobolich.lesson6_hw import palindrome


class Palindrome:
    def __init__(self, string: str):
        self.string = string

    def __bool__(self) -> bool:
        if (
            "errors" in palindrome(self.string)
            or not palindrome(self.string)["data"]  # noqa: W503
        ):
            return False
        return True


class User02:  # noqa: SIM119
    def __init__(self, birthday_date: date):
        self.age = get_formatted_birthday(birthday_date)["data"]["age"]


class HttpQuery03:
    def __init__(self, string: str):
        self.string = string

    def __getitem__(self, key: str) -> Any:
        try:
            http_query_parser(self.string)["data"][key]
        except KeyError:
            return None
        return http_query_parser(self.string)["data"][key]


class Multiplier04:
    def __init__(self) -> None:
        self.result = 1

    def add(self, arg: Any) -> Any:
        self.result *= multiply(arg)["data"]
        return self

    def get_result(self) -> Any:
        return self.result


class DupCounter05(collections.Counter):
    def __init__(self, collection: Collection) -> None:
        self.collection = collection
        self.result: dict = {}

    def get_dups(self) -> dict:
        counter_dict = collections.Counter(self.collection)
        for key, value in counter_dict.items():
            if value > 1:
                self.result[key] = value
        return self.result
