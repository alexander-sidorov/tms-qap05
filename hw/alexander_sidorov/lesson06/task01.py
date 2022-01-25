from typing import Union

from .common import Errors
from .common import api
from .common import typecheck


@api
@typecheck
def task_01(arg: str) -> Union[bool, Errors]:
    """
    Tells if the arg is a palindrome.
    """

    return arg == arg[::-1]
