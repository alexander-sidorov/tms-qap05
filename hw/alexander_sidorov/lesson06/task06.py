from typing import Union
from urllib.parse import parse_qs

from hw.alexander_sidorov.common import Errors
from hw.alexander_sidorov.common import api
from hw.alexander_sidorov.common import typecheck

Data = dict[str, list[str]]


@api
@typecheck
def task_06(query: str) -> Union[Data, Errors]:
    """
    Splits HTTP query into a dict.
    """

    data = parse_qs(
        query,
        keep_blank_values=True,
    )

    return data
