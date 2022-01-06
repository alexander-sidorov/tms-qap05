from hw.valeriya_mavritskaya.lesson06.homework06_functions import if_palindrome_1
from hw.valeriya_mavritskaya.lesson06.homework06_functions import multiplication_2
from hw.valeriya_mavritskaya.lesson06.homework06_functions import birthday_3
from hw.valeriya_mavritskaya.lesson06.homework06_functions import oldest_4
from datetime import date


def test_if_palindrome_1() -> None:
    assert if_palindrome_1("") == {'data': 'This is a palindrome'}
    assert if_palindrome_1("x") == {'data': 'This is a palindrome'}
    assert if_palindrome_1("xx") == {'data': 'This is a palindrome'}
    assert if_palindrome_1("xy") == {'data': 'This is not a palindrome'}
    assert if_palindrome_1(True) == {'error': 'Input must be a string'}
    assert if_palindrome_1("А муза рада музе без ума да разума") == {'data': 'This is a palindrome'}


def test_multiplication_2() -> None:
    assert multiplication_2(1) == {'data': 1}
    assert multiplication_2(1, 2) == {'data': 2}
    assert multiplication_2(1, 2, 3) == {'data': 6}
    assert multiplication_2(1, 2, 3, 8) == {'data': 48}
    assert multiplication_2(1, 2, 3, "dd") == {'error': 'Input must be a number'}


def test_birthday_3() -> None:
    assert birthday_3(date(year=1987, month=8, day=2)) == {'year': 1987, 'month': 8, 'day': 2, 'age': 34}
    assert birthday_3(1987) == {'error': 'Input must be a date'}


def test_oldest_4() -> None:
    assert oldest_4({"A": date(year=2000, month=5, day=4), "B": date(year=1855, month=4, day=3)}) == {'data': "B"}
    assert oldest_4({"A": date(1993, 8, 3), "B": date(2000, 6, 6), "C": date(1980, 4, 5)}) == {'data': "C"}
