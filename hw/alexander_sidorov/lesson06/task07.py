import re
from typing import Any
from typing import Optional
from typing import Union

from .common import Errors
from .common import api

RE_PAIR = re.compile(r"(\D\d+)")


@api
def task_07(folded_text: str) -> Union[str, Errors]:
    """
    Flattens the folded text in format <char><number of reps>.

    Example: a1b2a1 => abba
    """

    if errors := validate(folded_text):
        return errors

    folds = RE_PAIR.findall(folded_text)
    _folded_text = "".join(folds)
    if folded_text != _folded_text:
        return {"errors": [f"{folded_text=!r} is malformed"]}

    chars_counts = ((fold[0], int(fold[1:])) for fold in folds)

    flatten_text = "".join(char * count for char, count in chars_counts)

    return flatten_text


def validate(folded_text: Any) -> Optional[Errors]:
    if not isinstance(folded_text, str):
        return {"errors": [f"{type(folded_text)=!r}, MUST be a str"]}
    return None
