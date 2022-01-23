import re
from itertools import groupby
from typing import Any
from typing import Union

from .common import Errors
from .common import api
from .common import validate_args_types

RE_INTEGERS = re.compile(r".*\d")


@api
@validate_args_types
def task_08(flatten_text: str) -> Union[str, Errors]:
    """
    Folds the given text into the folded format:
    <char><number of reps>.

    Example: abba => a1b2a1
    """

    validate(flatten_text)

    folded_text = "".join(
        f"{char}{len(list(group))}" for char, group in groupby(flatten_text)
    )

    return folded_text


def validate(flatten_text: Any) -> None:
    assert not re.match(
        RE_INTEGERS, flatten_text
    ), "integers MUST not be present in flatten text"
