from hw.maria_saganovich.lesson5.task3 import func3


def test_func3() -> None:
    list3 = ["Santa Claus", "is", "coming", "to", "town"]
    part_of_list = list3[2]
    assert func3(list3, part_of_list) == ["Santa Claus", "is", "coming"]
