from hw.kirill_tobolich.lesson5_hw import encode_message
from hw.kirill_tobolich.lesson5_hw import first_and_last_collection_element
from hw.kirill_tobolich.lesson5_hw import slice_of_collection
from hw.kirill_tobolich.lesson5_hw import string_with_swapped_elements
from hw.kirill_tobolich.lesson5_hw import titled_string
from hw.kirill_tobolich.lesson5_hw import zipper


def test_example() -> None:
    list_for_test = [1, 3, 5, 8, 25]
    string_for_test = "Hello World"
    char_for_test = "b"
    object_for_test = 8
    text_for_test = "PYTHOn   is an interpreted high-level general-purpose programming  language."  # noqa: E501
    message_for_test = "VD DzgS PwFl DzgS SDK ZFz HD"
    key_for_test = "FTZHfrcwtoRgQzDaspdlKiPvSYLekVCqhJbyEnmMBAOIxuXjWUNG"
    assert first_and_last_collection_element(list_for_test) == (1, 25)
    assert string_with_swapped_elements(string_for_test) == "World Hello"
    assert slice_of_collection(list_for_test, object_for_test) == [1, 3, 5, 8]
    assert zipper(string_for_test, char_for_test) == "Hbeblblbob bWbobrblbdb"
    assert (
        titled_string(text_for_test)
        == "Python   Is An Interpreted High-Level General-Purpose Programming  Language."  # noqa: E501,W503
    )
    assert (
        encode_message(message_for_test, key_for_test)
        == "Do only what only you can do"  # noqa: W503
    )
