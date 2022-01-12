from urllib.parse import parse_qs

from .common import Result
from .common import build_result


def task_06(query: str) -> Result:
    """
    Splits HTTP query into a dict
    """

    if not isinstance(query, str):
        return build_result(errors=[f"{type(query)=!r}, MUST be a str"])

    data = parse_qs(
        query,
        keep_blank_values=True,
    )

    return build_result(data=data)
