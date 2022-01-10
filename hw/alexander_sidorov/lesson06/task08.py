import re
from itertools import groupby

from .common import Result

RE_INTEGERS = re.compile(r".*\d")


def task_08(flatten_text: str) -> Result:
    """
    Folds the given text into the folded format:
    <char><number of reps>
    """

    if re.match(RE_INTEGERS, flatten_text):
        return {"errors": ["integers MUST not be present in flatten text"]}

    folded_text = "".join(
        f"{char}{len(list(group))}" for char, group in groupby(flatten_text)
    )

    return {"data": folded_text}
