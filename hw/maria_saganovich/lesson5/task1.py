import operator


def func1(list1: list) -> tuple:
    first_last = operator.itemgetter(0, -1)
    result = first_last(list1)
    return tuple(result)
