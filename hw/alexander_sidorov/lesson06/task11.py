from .common import AnySet
from .common import Result
from .common import build_result


def task_11(arg1: AnySet, arg2: AnySet) -> Result:
    """
    Displays the common set of operations on two sets.
    """

    data = {
        "a&b": arg1 & arg2,
        "a|b": arg1 | arg2,
        "a-b": arg1 - arg2,
        "b-a": arg2 - arg1,
        "|a-b|": arg1 ^ arg2,
        "a in b": arg1.issubset(arg2),
        "b in a": arg2.issubset(arg1),
    }

    return build_result(data=data)
