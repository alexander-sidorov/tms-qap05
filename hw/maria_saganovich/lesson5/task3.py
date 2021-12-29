def func3(some_list: list, part_of_list: str) -> list:

    slice1 = slice(None, some_list.index(part_of_list) + 1)
    return some_list[slice1]
