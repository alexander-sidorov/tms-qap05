from typing import Any
from typing import Optional
from typing import Union
from urllib.parse import parse_qs

from .common import Errors
from .common import api

Data = dict[str, list[str]]


@api
def task_06(query: str) -> Union[Data, Errors]:
    """
    Splits HTTP query into a dict.
    """

    if errors := validate(query):
        return errors

    data = parse_qs(
        query,
        keep_blank_values=True,
    )

    return data


def validate(query: Any) -> Optional[Errors]:
    if not isinstance(query, str):
        return {"errors": [f"{type(query)=!r}, MUST be a str"]}
    return None
