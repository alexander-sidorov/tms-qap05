from typing import Any
from typing import Optional
from typing import Union

from .common import Errors
from .common import api


@api
def task_01(arg: str) -> Union[bool, Errors]:
    """
    Tells if the arg is a palindrome.
    """

    if errors := validate(arg):
        return errors

    rev = arg[::-1]
    data = bool(rev == arg)
    return data


def validate(arg: Any) -> Optional[Errors]:
    if not isinstance(arg, str):
        return {"errors": [f"{type(arg)=}, MUST be a string"]}

    return None
