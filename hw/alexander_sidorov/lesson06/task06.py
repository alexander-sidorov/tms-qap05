from typing import Union
from urllib.parse import parse_qs

from .common import Errors
from .common import api
from .common import validate_args_types

Data = dict[str, list[str]]


@api
@validate_args_types
def task_06(query: str) -> Union[Data, Errors]:
    """
    Splits HTTP query into a dict.
    """

    data = parse_qs(
        query,
        keep_blank_values=True,
    )

    return data
