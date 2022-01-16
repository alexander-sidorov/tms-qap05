from collections import Counter
from typing import Any
from typing import Collection
from typing import TypeVar

from .common import Errors
from .common import Undefined
from .common import api
from .common import build_result
from .common import hashable

T1 = TypeVar("T1")


@api
def task_05(collection: Collection[T1]) -> Any:
    """
    Calculates count of duplicates in the given collection
    """

    data: Any = Undefined
    errors: Errors = []

    for i, elem in enumerate(collection):
        if not hashable(elem):
            errors.append(f"collection[{i}]={elem!r}, not hashable")

    if not errors:
        ctr = Counter(collection)
        data = {elem: count for elem, count in ctr.items() if count > 1}
        return data

    return build_result(errors=errors)
