import re
from itertools import groupby

from .common import Result
from .common import build_result

RE_INTEGERS = re.compile(r".*\d")


def task_08(flatten_text: str) -> Result:
    """
    Folds the given text into the folded format:
    <char><number of reps>
    """

    if not isinstance(flatten_text, str):
        return build_result(errors=[f"{type(flatten_text)=!r}, MUST be a str"])

    if re.match(RE_INTEGERS, flatten_text):
        return build_result(
            errors=["integers MUST not be present in flatten text"]
        )

    data = "".join(
        f"{char}{len(list(group))}" for char, group in groupby(flatten_text)
    )

    result = build_result(data=data)

    return result
