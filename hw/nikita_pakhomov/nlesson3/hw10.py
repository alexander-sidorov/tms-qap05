from datetime import date
from typing import Any

from hw.nikita_pakhomov.nlesson3.hw6 import palindrome


class Palindrome01:
    def __init__(self, stroka: Any) -> None:
        self.stroka = stroka

    def __bool__(self) -> Any:
        return palindrome(self.stroka)


class User02:
    def __init__(self, born: date) -> None:
        self.born = born

    def age(self) -> Any:
        today = date.today()
        return today.year - self.born.year - ((today.month, today.day) < (self.born.month, self.born.day)) # noqa:
