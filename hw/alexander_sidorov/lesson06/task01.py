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
