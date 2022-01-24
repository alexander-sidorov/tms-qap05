from collections import Counter
from typing import Any
from typing import Collection
from typing import TypeVar
from typing import Union

from .common import Errors
from .common import api
from .common import hashable
from .common import validate_args_types

T1 = TypeVar("T1")


Data = dict[T1, int]


@api
@validate_args_types
def task_05(collection: Collection[T1]) -> Union[Data, Errors]:
    """
    Calculates count of duplicates in the given collection.
    """

    validate(collection)

    ctr = Counter(iter(collection))
    data = {elem: count for elem, count in ctr.items() if count > 1}
    return data


def validate(collection: Any) -> None:
    for i, elm in enumerate(collection):
        assert hashable(elm), f"collection[{i}]={elm!r} is not hashable"
