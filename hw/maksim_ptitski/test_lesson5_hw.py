from hw.maksim_ptitski.lesson5_hw import combine_result
from hw.maksim_ptitski.lesson5_hw import first_and_last_collection_element
from hw.maksim_ptitski.lesson5_hw import separated_string
from hw.maksim_ptitski.lesson5_hw import string_with_capitalized_letters
from hw.maksim_ptitski.lesson5_hw import two_words_reversed


def test_hw_5() -> None:
    list_for_test = [1, 3, 5, 9, 25, 63, 100]
    string_for_test = "Maksim Ptitski"
    char_for_test = "o"
    object_for_test = 9
    text_for_test = "PYTHOn   is an interpreted high-level general-purpose programming  language."  # noqa: E501
    assert first_and_last_collection_element(list_for_test) == (1, 100)
    assert two_words_reversed(string_for_test) == "Ptitski Maksim"
    assert combine_result(list_for_test, object_for_test) == [1, 3, 5, 9]
    assert (
        separated_string(string_for_test, char_for_test)
        == "Moaokosoiomo oPotoiotosokoi"  # noqa: W503
    )
    assert (
        string_with_capitalized_letters(text_for_test)
        == "Python   Is An Interpreted High-Level General-Purpose Programming  Language."  # noqa: E501,W503
    )
