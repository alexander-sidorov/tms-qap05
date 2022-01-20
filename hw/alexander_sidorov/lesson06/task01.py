from typing import Any
from typing import Optional
from typing import Union

from .common import Errors
from .common import api
from .common import validate_args_types


@api
@validate_args_types
def task_01(arg: str) -> Union[bool, Errors]:
    """
    Tells if the arg is a palindrome.
    """

    return arg == arg[::-1]


def validate(arg: Any) -> Optional[Errors]:
    if not isinstance(arg, str):
        return {"errors": [f"{type(arg)=}, MUST be a string"]}

    return None
