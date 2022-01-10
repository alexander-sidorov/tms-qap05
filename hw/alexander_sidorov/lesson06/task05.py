from collections import Counter
from typing import Collection
from typing import Hashable
from typing import List
from typing import TypeVar

from .common import Result

T1 = TypeVar("T1")


def task_05(collection: Collection[T1]) -> Result:
    """
    Calculates count of duplicates in the given collection
    """

    elem: T1

    errors: List[str] = []

    for i, elem in enumerate(collection):
        if not isinstance(elem, Hashable):
            errors.append(f"collection[{i}]={elem!r} is not hashable")

    if errors:
        return {"errors": errors}

    ctr = Counter(collection)
    data = {elem: count for elem, count in ctr.items() if count > 1}
    return {"data": data}
