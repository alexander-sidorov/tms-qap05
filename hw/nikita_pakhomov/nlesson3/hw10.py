from typing import Any

from hw.nikita_pakhomov.nlesson3.hw6 import is_palindrome


class Palindrome01:
    def __init__(self, stroka: Any) -> None:
        self.stroka = stroka

    def __ccc__(self) -> Any:
        return is_palindrome(self.stroka)
