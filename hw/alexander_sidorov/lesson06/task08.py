import re
from itertools import groupby
from typing import Any
from typing import Optional
from typing import Union

from .common import Errors
from .common import ErrorsList
from .common import api

RE_INTEGERS = re.compile(r".*\d")


@api
def task_08(flatten_text: str) -> Union[str, Errors]:
    """
    Folds the given text into the folded format:
    <char><number of reps>.

    Example: abba => a1b2a1
    """

    if errors := validate(flatten_text):
        return errors

    folded_text = "".join(
        f"{char}{len(list(group))}" for char, group in groupby(flatten_text)
    )

    return folded_text


def validate(flatten_text: Any) -> Optional[Errors]:
    messages: ErrorsList = []

    if not isinstance(flatten_text, str):
        messages.append(f"{type(flatten_text)=!r}, MUST be a str")
    else:
        if re.match(RE_INTEGERS, flatten_text):
            messages.append("integers MUST not be present in flatten text")

    return {"errors": sorted(messages)} if messages else None
