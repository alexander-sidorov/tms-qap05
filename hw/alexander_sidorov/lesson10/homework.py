from collections import Counter
from datetime import date
from typing import Any
from typing import Callable
from typing import Generic
from typing import Literal
from typing import Optional
from typing import TypeVar
from typing import Union
from typing import cast
from urllib.parse import parse_qs

from typing_extensions import ParamSpec

from hw.alexander_sidorov.lesson06.task01 import task_01
from hw.alexander_sidorov.lesson06.task02 import task_02
from hw.alexander_sidorov.lesson06.task03 import task_03

Params = ParamSpec("Params")
T1 = TypeVar("T1")
T2 = TypeVar("T2")
TSM1 = dict[str, Union[T1, list[T1]]]

DataKey = Union[
    Literal["data"],
    Literal["errors"],
]


class Arity1(Generic[T1]):
    def __init__(self, arg: T1) -> None:
        self._arg = arg


class Palindrome01(Arity1[str]):
    def __bool__(self) -> bool:
        result = cast(bool, extract_data(task_01, self._arg))
        return result


class User02(Arity1[date]):
    @property
    def age(self) -> int:
        data = extract_data(task_03, self._arg)
        age = cast(int, data["age"])
        return age


class HttpQuery03(Arity1[str]):
    def __init__(self, query: str):
        super().__init__(query)
        self.__kw: TSM1 = {}

    def __getitem__(self, key: str) -> Optional[list[str]]:
        self.__parse()

        value = self.__kw.get(key)
        if isinstance(value, list) and len(value) == 1:
            value = value[0]

        return value

    def __parse(self) -> None:
        if self.__kw:
            return

        self.__kw = parse_qs(
            self._arg,
            keep_blank_values=True,
        )


class Multiplier04:
    def __init__(self) -> None:
        self.__args: list[Any] = []

    def add(self, value: Any) -> "Multiplier04":
        self.__args.append(value)
        return self

    def get_result(self) -> Any:
        result = extract_data(task_02, *self.__args)
        return result


class DupCounter05(Counter):
    def get_dups(self) -> dict:
        return {k: v for k, v in self.items() if v > 1}


def extract_data(func: Callable[[T1], dict[DataKey, T2]], *args: T1) -> T2:
    result = func(*args)
    assert result
    assert isinstance(result, dict)
    assert "data" in result
    assert "errors" not in result
    data = result["data"]
    return data
