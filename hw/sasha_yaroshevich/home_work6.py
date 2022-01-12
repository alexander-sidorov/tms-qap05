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

def date_rojdeniya(*args):
    result = {}

    if len(args) != 3:
        result["errors"] = ["vveli ne datu. Nujno 3 chisla"]
    else:
        d_1, d_2, d_3 = args
        date_vvedennoe = date(year=d_1, month=d_2, day=d_3)
        current_datetime = datetime.now()
        date_now = current_datetime.year
        age = date_now - date_vvedennoe
        result["data"] = {"year": d_1, "month": d_2, "day": d_3, "age": age}