from hw.andrey_yelin.Lesson_05.yelin_lesson05hw import first_last_elements
from hw.andrey_yelin.Lesson_05.yelin_lesson05hw import slice_of_col03
from hw.andrey_yelin.Lesson_05.yelin_lesson05hw import string_combination
from hw.andrey_yelin.Lesson_05.yelin_lesson05hw import swapped_words
from hw.andrey_yelin.Lesson_05.yelin_lesson05hw import titled_string


def test_example05() -> None:
    col01 = [1 + 1j, 1 - 1j, 0]
    col02 = "bbbbbbbb                             aaaaaaaa"
    some_object = 1 - 1j
    string01 = "j"
    string02 = "FOR the glory of the Emperor"
    assert first_last_elements(col01) == (1 + 1j, 0)
    assert swapped_words(col02) == "aaaaaaaa bbbbbbbb"
    assert slice_of_col03(col01, some_object) == [1 + 1j, 1 - 1j]
    assert (
        string_combination(string02, string01)
        == "FjOjRj jtjhjej jgjljojrjyj jojfj jtjhjej jEjmjpjejrjojr"  # noqa: W503, E501
    )
    assert titled_string(string02) == "For The Glory Of The Emperor"
