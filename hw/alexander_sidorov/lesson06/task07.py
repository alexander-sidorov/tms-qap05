import re

from .common import Result
from .common import build_result

RE_PAIR = re.compile(r"(\D\d+)")


def task_07(folded_text: str) -> Result:
    """
    Flattens the folded text in format <char><number of reps>
    """

    if not isinstance(folded_text, str):
        return build_result(errors=[f"{type(folded_text)=!r}, MUST be a str"])

    folds = RE_PAIR.findall(folded_text)
    _folded_text = "".join(folds)
    if folded_text != _folded_text:
        return build_result(errors=[f"{folded_text=!r} is malformed"])

    chars_counts = ((fold[0], int(fold[1:])) for fold in folds)

    flatten_text = "".join(char * count for char, count in chars_counts)

    return build_result(data=flatten_text)
