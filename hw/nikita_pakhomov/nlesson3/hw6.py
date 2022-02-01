from datetime import date
from typing import Any
from typing import Dict

Result = Dict[str, Any]
type_1 = Dict[str, Any]


def decorate(func: Any) -> Any:
    def xxx(*args: Any) -> Any:
        result = func(*args)
        if result == "invalid input":  # noqa
            return {"errors": [result]}
        else:
            return {"data": result}

    return xxx


@decorate
def is_palindrome(text: Any) -> Any:
    if not isinstance(text, str):
        result = "invalid input"
        return result
    if text[:] == text[::-1]:  # noqa
        return True
    else:
        return False


def palindrome(text: str) -> Any:
    if not isinstance(text, str):
        result = False
        return result
    if text[:] == text[::-1]:
        result = True
    else:
        result = False
    return result


@decorate
def level_2(*args: Any) -> Any:
    nakopitel = 1

    for i in args:
        if not isinstance(i, int):
            result = "invalid input"
            return result
        nakopitel *= i

    return nakopitel


@decorate
def level_3(born: Any) -> Any:
    result = {}
    if not isinstance(born, date):
        return "invalid input"
    today = date.today()
    try:
        birthday = born.replace(year=today.year)
    except ValueError:
        birthday = born.replace(year=today.year, month=born.month + 1, day=1)
    if birthday > today:
        age = today.year - born.year - 1
        result = {
            "year": born.year,
            "month": born.month,
            "day": born.day,
            "age": age,
        }
        return result
    else:
        age = today.year - born.year
        result = {
            "year": born.year,
            "month": born.month,
            "day": born.day,
            "age": age,
        }
        return result


@decorate
def level_4_1(age: Any) -> Any:
    if not isinstance(age, dict):
        return "invalid input"
    name = min(age, key=lambda n: age[n])  # noqa
    return name


@decorate
def level_5(spisok: Any) -> Any:
    result: dict = {}
    clovar: dict = {}
    if not isinstance(spisok, list):
        return "invalid input"
    for iii in spisok:
        if iii in clovar:
            clovar[iii] = clovar[iii] + 1
        else:
            clovar[iii] = 1
    for yyy in spisok:
        if clovar[yyy] <= 1:
            del clovar[yyy]
    result = clovar
    return result


@decorate
def level_7(stroka: Any) -> Any:
    stroch = ""
    otvet = ""
    cpisok = []
    otvett = ""
    if not isinstance(stroka, str):
        return "invalid input"
    stroka = stroka + "="
    for iii in range(len(stroka)):
        if stroka[iii].isdecimal():
            stroch = stroch + stroka[iii]
        elif stroka[iii].isalnum():
            otvet = otvet + stroka[iii]
            if stroch != "":
                cpisok.append(stroch)
                stroch = ""
        elif stroka[iii] == "=":
            cpisok.append(stroch)
            stroch = ""
    if len(cpisok) != len(otvet):
        return "invalid input"
    for yyy in range(len(otvet)):
        otvett = otvett + (otvet[yyy] * int(cpisok[yyy]))
    return otvett


@decorate
def level_8(string: Any) -> Any:
    if not isinstance(string, str):
        return "invalid input"
    if string == "":
        return ""
    counter = 0
    ppp = string[0]
    calo = ""
    for iii in range(len(string)):
        if ppp == string[iii]:
            counter = counter + 1
        else:
            calo = calo + (ppp + str(counter))
            counter = 1
        ppp = string[iii]
    calo = calo + (ppp + str(counter))
    return calo
