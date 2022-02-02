import re
from typing import Sequence
from typing import Union

from hw.alexander_sidorov.common import Errors
from hw.alexander_sidorov.common import api
from hw.alexander_sidorov.common import typecheck

RE_PAIR = re.compile(r"(\D\d+)")


@api
@typecheck
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
    correct = folded_text == restored
    assert correct, f"{folded_text=!r} is malformed"
