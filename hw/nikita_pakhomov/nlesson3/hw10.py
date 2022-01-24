from typing import Any

from hw.nikita_pakhomov.nlesson3.hw6 import palindrome


class Palindrome01:
    def __init__(self, stroka: Any) -> bool:
        self.stroka = stroka

    def __bool__(self) -> Any:
        return palindrome(self.stroka)
