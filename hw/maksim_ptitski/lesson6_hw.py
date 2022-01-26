import collections
import re
from collections import Counter
from datetime import date
from typing import Any
from typing import Callable
from typing import Collection
from typing import Sequence

ERROR_NOT_STRING = "given argument is not string type"
ERROR_NOT_LIST_STR_TUPLE = (
    "given argument with keys is not a list, str or tuple"
)
ERROR_WRONG_FORMAT_OF_STR = "wrong format of string"
ERROR_UNHASHABLE_TYPE = "unhashable type: 'dict'"


def decorator_dict(func: Callable) -> Callable:
    def wrapper(*a: Any, **kw: Any) -> Any:
        try:
            result = func(*a, **kw)
            return {"data": result}
        except Exception as err:
            return {"errors": [str(err)]}

    return wrapper


@decorator_dict
def palindrome(string: str) -> Any:
    assert isinstance(string, str), ERROR_NOT_STRING
    return string == string[::-1]


@decorator_dict
def multiply(*args: Any) -> Any:
    result = 0
    assert isinstance(args, (int, float, complex, Sequence)), [
        "given arguments' types can't be multiplied"
    ]
    assert len(args) != 0, "no argument is given"
    if len(args) == 1:
        result = args[0]
    else:
        multiplication_result = 1
        for i in args:
            multiplication_result *= i
            result = multiplication_result
    return result


@decorator_dict
def get_formatted_birthday(birthday_date: date) -> dict:
    assert isinstance(
        birthday_date, date
    ), "given argument is not object of date type"
    today = date.today()
    birthday_this_year = date(
        today.year, birthday_date.month, birthday_date.day
    )
    if birthday_this_year > today:
        age = today.year - birthday_date.year - 1
    else:
        age = today.year - birthday_date.year
    result = {
        "year": birthday_date.year,
        "month": birthday_date.month,
        "day": birthday_date.day,
        "age": age,
    }
    return result


@decorator_dict
def get_the_eldest(dictionary: dict[Any, date]) -> Any:
    assert isinstance(dictionary, dict), "Given argument is not a dictionary"
    for _key, value in dictionary.items():
        assert isinstance(value, date), "key value is not object of date type"
    min_value = min(dictionary, key=lambda k: dictionary[k])
    result = min_value
    return result


@decorator_dict
def get_the_same_elements_in_collection(collection: Any) -> dict:
    assert isinstance(collection, Collection), ERROR_NOT_LIST_STR_TUPLE
    counter: Counter = collections.Counter(collection)
    result_dict = {}
    for key, value in counter.items():
        if value == 1:
            continue
        else:
            result_dict[key] = value
    result = result_dict
    return result


@decorator_dict
def http_query_parser(query: str) -> dict:
    assert isinstance(query, str), ERROR_NOT_STRING
    dict_with_queries = {}
    split_query = query.split("&")
    for i in split_query:
        index_of_equals = i.index("=")
        name = i[:index_of_equals]
        if name not in dict_with_queries:
            dict_with_queries[name] = [i[index_of_equals + 1 :]]  # noqa: E203
        else:
            dict_with_queries[name].append(
                i[index_of_equals + 1 :]  # noqa: E203
            )  # noqa: E203
    result = dict_with_queries
    return result


@decorator_dict
def repeat_chars(string: str) -> Any:
    assert isinstance(string, str), ERROR_NOT_STRING
    numbers = re.findall(r"\d+", string)
    chars = re.findall(r"\D", string)
    assert len(numbers) == len(chars), ERROR_WRONG_FORMAT_OF_STR
    zipped_lists = list(zip(numbers, chars))
    result_str = ""
    for num, char in zipped_lists:
        result_str += char * int(num)
    return result_str


@decorator_dict
def count_chars(string: str) -> Any:
    assert isinstance(string, str), ERROR_NOT_STRING
    if len(string) == 0:
        result = ""
        return result
    if len(string) == 1:
        result = f"{string[0]}1"
        return result
    result_str = ""
    counter: dict = {string[0]: 0}
    previous_value = string[0]
    for letter in string:
        if letter in counter:
            counter[letter] += 1
        else:
            counter[letter] = 1
            substring = f"{previous_value}{counter[previous_value]}"
            result_str += substring
            counter.pop(previous_value)
            previous_value = letter
    result_str += f"{list(counter.keys())[0]}{list(counter.values())[0]}"
    result = result_str
    return result


@decorator_dict
def inverted_dictionary(dictionary: dict) -> dict:
    assert isinstance(dictionary, dict), "given argument is not dict type"
    inverted_dict = {}
    for key, value in dictionary.items():
        if value not in inverted_dict:
            inverted_dict[value] = [key]
        else:
            inverted_dict[value].append(key)
    for new_key, new_value in inverted_dict.items():
        if len(new_value) < 2:
            inverted_dict[new_key] = new_value[0]
    result = inverted_dict
    return result


@decorator_dict
def zip_collections_to_dict(keys: Any, values: Any) -> dict:
    assert isinstance(keys, Sequence), "first given argument is not Sequence"
    assert isinstance(
        values, Collection
    ), "second given argument is not Collection"
    keys = list(keys)
    values = list(values)
    if len(keys) > len(values):
        differance = len(keys) - len(values)
        values.extend(None for _ in range(differance))
        list_of_zipped_collections = list(zip(keys, values))
        result = dict(list_of_zipped_collections)
    elif len(keys) < len(values):
        differance_list = values[len(keys) :]  # noqa: E203
        list_with_the_same_length = values[: len(keys)]
        list_of_zipped_collections = list(zip(keys, list_with_the_same_length))
        list_of_zipped_collections.append(("...", differance_list))
        result = dict(list_of_zipped_collections)
    else:
        list_of_zipped_collections = list(zip(keys, values))
        result = dict(list_of_zipped_collections)
    return result


@decorator_dict
def relations_between_two_sets(set1: set, set2: set) -> dict:
    assert isinstance(set1, set), "given first argument is not set type"
    assert isinstance(set2, set), "given second argument is not set type"
    return {
        "a&b": set1 & set2,
        "a|b": set1 | set2,
        "a-b": set1 - set2,
        "b-a": set2 - set1,
        "|a-b|": set1 ^ set2,
        "a in b": set1.issubset(set2),
        "b in a": set2.issubset(set1),
    }


@decorator_dict
def make_dictionary(*args: Any) -> dict:
    assert len(args) % 2 == 0, "Quantity of given arguments is not even"
    keys = []
    values = []
    for i in args:
        if args.index(i) % 2 == 0:
            keys.append(i)
        else:
            values.append(i)
    dictionary_from_arguments = dict(list(zip(keys, values)))
    result = dictionary_from_arguments
    return result
