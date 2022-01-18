from collections import Counter
from typing import Any
from typing import Collection
from typing import Optional
from typing import TypeVar
from typing import Union

from .common import Errors
from .common import ErrorsList
from .common import api
from .common import hashable

T1 = TypeVar("T1")


Data = dict[T1, int]


@api
def task_05(collection: Collection[T1]) -> Union[Data, Errors]:
    """
    Calculates count of duplicates in the given collection.
    """

    if errors := validate(collection):
        return errors

    ctr = Counter(iter(collection))
    data = {elem: count for elem, count in ctr.items() if count > 1}
    return data


def validate(collection: Any) -> Optional[Errors]:
    messages: ErrorsList = []

    if not isinstance(collection, Collection):
        messages.append(f"{type(collection)=!r}, MUST be a collection")
    else:
        messages.extend(
            f"collection[{i}]={elem!r} is not hashable"
            for i, elem in enumerate(collection)
            if not hashable(elem)
        )

    return {"errors": sorted(messages)} if messages else None
