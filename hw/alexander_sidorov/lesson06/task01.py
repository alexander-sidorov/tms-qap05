from typing import Union

from hw.alexander_sidorov.common import Errors
from hw.alexander_sidorov.common import api
from hw.alexander_sidorov.common import typecheck


@api
@typecheck
def task_01(arg: str) -> Union[bool, Errors]:
    """
    Tells if the arg is a palindrome.
    """

    return arg == arg[::-1]
