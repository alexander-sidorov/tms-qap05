from collections import Counter
from typing import Any

from hw.siarhei_apanel.refakt import dateday
from hw.siarhei_apanel.refakt import html_str
from hw.siarhei_apanel.refakt import palindrom
from hw.siarhei_apanel.refakt import proizvedenie
from hw.siarhei_apanel.refakt import repeat


class Palindrome01:
    def __init__(self, text: Any) -> None:
        self.text = text

    def __bool__(self) -> Any:
        result = palindrom(self.text)
        return result["data"]


class Multiplier04:
    def __init__(self) -> None:
        self.arg: list[Any] = []

    def add(self, arg: Any) -> Any:
        self.arg.append(arg)
        return self

    def get_result(self) -> Any:
        result = proizvedenie(*self.arg)
        assert "errors" not in result, str(result["errors"])

        return result["data"]


class User02:
    def __init__(self, datee: Any) -> None:
        self.datee = datee

    @property
    def age(self) -> Any:
        result = dateday(self.datee)
        assert "errors" not in result, str(result["errors"])
        return result["data"]["age"]


class DupCounter05(Counter):
    def __init__(self, coll: Any) -> None:
        self.coll = coll

    def get_dups(self) -> Any:
        result = repeat(self.coll)
        assert "errors" not in result, str(result["errors"])
        return result["data"]


class HttpQuery03:
    def __init__(self, text: Any) -> None:
        self.text = text
        self.diction: dict[Any, Any] = {}

    def __getitem__(self, key: Any) -> Any:
        self.diction = html_str(self.text)
        assert "errors" not in self.diction, str(self.diction["errors"])
        result = self.diction["data"].get(key)
        if isinstance(result, list) and len(result) < 2:
            return result[0]
        return result
