from hw.andrey_yelin.Lesson_05.yelin_lesson05hw import first_last_elements
from hw.andrey_yelin.Lesson_05.yelin_lesson05hw import slice_of_col03
from hw.andrey_yelin.Lesson_05.yelin_lesson05hw import string_combination
from hw.andrey_yelin.Lesson_05.yelin_lesson05hw import swapped_words
from hw.andrey_yelin.Lesson_05.yelin_lesson05hw import titled_string


def test_example05() -> None:
    col01 = [1, 2, 3, 4, 5, 6, 7]
    col02 = "tuda suda"
    some_object = 6
    string01 = "j"
    string02 = "FOR the glory of the Emperor"
    assert first_last_elements(col01) == (1, 7)
    assert swapped_words(col02) == "suda tuda"
    assert slice_of_col03(col01, some_object) == [1, 2, 3, 4, 5, 6]
    assert (
        string_combination(string01, string02)
        == "FjOjRj jtjhjej jgjljojrjyj jojfj jtjhjej jEjmjpjejrjojr"  # noqa: W503
    )
    assert titled_string(string02) == "For The Glory Of The Emperor"
