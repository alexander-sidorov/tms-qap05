import re

from .common import Result


def task_07(folded_text: str) -> Result:
    """
    Flattens the folded text in format <char><number of reps>
    """

    folds = re.findall(r"(\D\d+)", folded_text)
    if "".join(folds) != folded_text:
        return {"errors": [f"{folded_text=!r} is malformed"]}

    chars_counts = ((fold[0], int(fold[1:])) for fold in folds)

    flatten_text = "".join(char * count for char, count in chars_counts)

    return {"data": flatten_text}
