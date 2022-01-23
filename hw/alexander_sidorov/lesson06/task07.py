import re
from typing import Sequence
from typing import Union

from .common import Errors
from .common import api
from .common import validate_args_types

RE_PAIR = re.compile(r"(\D\d+)")


@api
@validate_args_types
def task_07(folded_text: str) -> Union[str, Errors]:
    """
    Flattens the folded text in format <char><number of reps>.

    Example: a1b2a1 => abba
    """

    folds = RE_PAIR.findall(folded_text)
    validate_folds(folded_text, folds)

    chars_counts = ((fold[0], int(fold[1:])) for fold in folds)

    flatten_text = "".join(char * count for char, count in chars_counts)

    return flatten_text


def validate_folds(folded_text: str, folds: Sequence[str]) -> None:
    restored = "".join(folds)
    ok = folded_text == restored
    assert ok, f"{folded_text=!r} is malformed"
