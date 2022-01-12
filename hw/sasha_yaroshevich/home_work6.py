from typing import Any
from typing import Dict
from datetime import date, datetime


new_type = Dict[str, Any]
def polindrom_1(stroka: str) -> new_type:
    result = {}

    if type(stroka) != str:
        result["errors"] = ["this is not a string"]
    else:
        if stroka == stroka[::-1]:
            result["data"] = True
        else:
            result["data"] = False
    return result


def proizvedenie_2(*args):
    result = {}


    nakopitel = 1
    for i in args:
        nr = isinstance(nakopitel, (str, list, tuple))
        er = isinstance(i, (str, list, tuple))
        if nr and er:
            result["errors"] = ["stroki, niz9"]
        else:
            nakopitel *= i

        result["data"] = nakopitel
    return result

def date_rojdeniya_3(date_v):
    result = {}

    if date_v.year >= 2022:
        result["errors"] = ["ne rodilsya"]
    else:


        now = datetime.now()
        then = datetime(date_v.year, date_v.month, date_v.day)
        delta = now - then
        age = delta.days // 365

        new_dict = {"year": date_v.year, "month": date_v.month, "day": date_v.day, "age": age}
        result["data"] = new_dict
    return result