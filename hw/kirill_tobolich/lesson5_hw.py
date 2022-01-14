from typing import Any


def first_and_last_collection_element(collection: Any) -> tuple:
    return collection[0], collection[-1]


def string_with_swapped_elements(string: str) -> str:
    string_to_list = string.rsplit()
    return f"{string_to_list[1]} {string_to_list[0]}"


def slice_of_collection(collection: Any, object_of_collection: Any) -> Any:
    index = collection.index(object_of_collection)
    return collection[: index + 1]


def zipper(string1: str, string2: str) -> str:
    zipped_string = ""
    for i in string1:
        zipped_string += i + string2
    return zipped_string


def titled_string(any_string: str) -> str:
    return any_string.title()


def encode_message(message: str, key: str) -> str:
    alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    encoded_message = ""
    for i in message:
        if i == " ":
            encoded_message += " "
            continue
        else:
            index = key.find(i)
            letter = alphabet[index]
            encoded_message += letter
    return encoded_message
