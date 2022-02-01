from typing import Any

from hw.nikita_pakhomov.nlesson3.hw6 import level_3
from hw.nikita_pakhomov.nlesson3.hw6 import palindrome


class Palindrome01:
    def __init__(self, stroka: Any) -> None:
        self.stroka = stroka

    def __bool__(self) -> Any:
        return palindrome(self.stroka)


class User02:
    def __init__(self, bd: Any) -> None:
        self.bd = level_3(bd)

    @property
    def age(self) -> Any:
        return self.bd["data"]["age"]
