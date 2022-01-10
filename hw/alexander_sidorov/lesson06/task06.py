from urllib.parse import parse_qs

from .common import Result


def task_06(query: str) -> Result:
    """
    Splits HTTP query into a dict
    """

    parsed = parse_qs(
        query,
        keep_blank_values=True,
    )

    return {"data": parsed}
