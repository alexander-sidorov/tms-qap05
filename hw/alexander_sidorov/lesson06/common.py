from typing import Any
from typing import Any
from typing import Dict
from typing import FrozenSet
from typing import List
from typing import Set
from typing import TypeVar
from typing import TypeVar
from typing import Union
from typing import Union

AnySet = Union[Set, FrozenSet]
Result = Dict[str, Any]
T1 = TypeVar("T1")
T2 = TypeVar("T2")


class UndefinedType:
    pass


Undefined = UndefinedType()


def build_result(
    *,
    data: Any = Undefined,
    errors: Union[List[str], UndefinedType] = Undefined,
) -> Result:
    result: Result = {}

    if errors and errors is not Undefined:
        assert isinstance(errors, list)
        result["errors"] = sorted(errors)

    if not result and data is not Undefined:
        result["data"] = data

    return result


def even(arg: int) -> bool:
    return arg % 2 == 0
