from typing import Dict, Any
from datetime import date
from math import prod
import collections

Result = Dict[str, Any]


def if_palindrome_1(u_input: str) -> dict:
    result = {}
    if isinstance(u_input, str):
        u_input = u_input.lower()
        u_input = u_input.replace(" ", "")
        list1 = list(u_input)
        list2 = list(u_input)
        list2.reverse()
        if list1 == list2:
            result["data"] = "This is a palindrome"
        else:
            result["data"] = "This is not a palindrome"
    else:
        result["error"] = "Input must be a string"
    return result


def multiplication_2(*args: int) -> dict:
    result = {}
    if any(not isinstance(item, int) for item in args):
        result["error"] = "Input must be a number"
    else:
        result["data"] = prod(args)
    return result


def birthday_3(input_date: date) -> dict:
    result = {}
    if isinstance(input_date, date):
        now = date.today()
        age = int((now - input_date).days)
        age = round(age / 365)
        result = {
            "year": input_date.year,
            "month": input_date.month,
            "day": input_date.day,
            "age": age
            }
    else:
        result["error"] = "Input must be a date"
    return result


def oldest_4(people: dict) -> dict:
    result = {}
    if not isinstance(people, dict):
        result["error"] = "Input must be a dictionary"
    elif any(not isinstance(p, date) for p in people.values()):
        result["error"] = "Input must contain date"
    else:
        result["data"] = f"{min(people, key=people.get)}"
    return result


def duplicates_5(collection: list) -> dict:
    result = {}
    select_duplicates = {i: collection.count(i) for i in collection}
    duplicates_add_count = {key: value for (key, value) in select_duplicates.items() if value > 1}
    result["data"] = duplicates_add_count
    return result


def count_amount_8(str_input: str) -> dict:
    result = {}
    count = collections.Counter(str_input)
    create_str = (f"{key}{value}" for (key, value) in count.items())
    result["data"] = "".join(create_str)
    return result


def mk_dictionary_12(*args) -> Result:
    result: Result = {}
    result = {args[i]: args[i + 1] for i in range(0, len(args), 2)}
    return result


if __name__ == '__main__':
    print(if_palindrome_1("А муза рада музе без ума да разума"))
    print(if_palindrome_1("bп"))
    print(if_palindrome_1(True))

    print(multiplication_2(1, 2, 3, 8))
    print(multiplication_2((1, 2, 3, "dd")))

    print(birthday_3(date(1993, 8, 3)))
    print(birthday_3(1993))

    print(oldest_4({"A": date(1993, 8, 3), "B": date(1993, 8, 3)}))
    print(oldest_4({"A": date(year=2000, month=5, day=4), "B": date(year=1855, month=4, day=3)}))
    print(oldest_4(1993))

    print(duplicates_5([(), '', '', 1]))
    print(duplicates_5([(), "", "", 1, 5, 7, 7, True, True]))
    print(duplicates_5([]))

    print(count_amount_8("aaabb"))

    print(mk_dictionary_12(1, 8, 5, 5))
