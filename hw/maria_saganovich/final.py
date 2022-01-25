from dataclasses import dataclass
from typing import Any

from hw.maria_saganovich.lesson6_hw.lvl1_palindrome import func1_palindrome
from hw.maria_saganovich.lesson6_hw.lvl3_age import func3_age
from hw.maria_saganovich.lesson6_hw.lvl5_duplicate_elements import (
    func5_duplicate_elements,
)
from hw.maria_saganovich.lesson6_hw.lvl6_dict_http_query import (
    func6_dict_http_query,
)


class Palindrome01:
    def __init__(self, text: Any) -> None:
        self.text = text

    def __bool__(self) -> Any:
        result = func1_palindrome(self.text)
        if "errors" in result:
            return result
        return result["data"]


@dataclass(unsafe_hash=True)
class User02:
    def __init__(self, date: Any) -> None:
        self.user_info = func3_age(date)
        if "errors" in self.user_info:
            self.age = self.user_info
        else:
            self.age = self.user_info["data"]["age"]


class HttpQuery03:
    def __init__(self, text: Any) -> None:
        self.text = text
        self.dict_http_query: dict = {}

    def __getitem__(self, key: Any) -> Any:
        self.dict_http_query = func6_dict_http_query(self.text)
        if "errors" in self.dict_http_query:
            return self.dict_http_query
        return self.dict_http_query["data"].get(key)


class Multiplier04:
    def __init__(self) -> None:
        self.number = 1

    def add(self, number: Any) -> Any:
        self.number *= number
        return self

    def get_result(self) -> Any:
        return self.number


class DupCounter05:
    def __init__(self, data: Any) -> None:
        self.data = data

    def get_dups(self) -> Any:
        result = func5_duplicate_elements(self.data)
        if "errors" in result:
            return result
        return result["data"]
