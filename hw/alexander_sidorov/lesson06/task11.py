from typing import Literal
from typing import Union

from hw.alexander_sidorov.common import AnySet
from hw.alexander_sidorov.common import Errors
from hw.alexander_sidorov.common import api
from hw.alexander_sidorov.common import typecheck

DataKeys = Literal[
    "|a-b|",
    "a in b",
    "a-b",
    "a&b",
    "a|b",  # type: ignore
    "b in a",
    "b-a",
]

Data = dict[DataKeys, Union[AnySet, bool]]


@api
@typecheck
def task_11(arg1: AnySet, arg2: AnySet) -> Union[Data, Errors]:
    """
    Displays the common set of operations upon two sets.
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

    return data
