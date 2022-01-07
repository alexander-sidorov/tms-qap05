from typing import Any
from typing import Dict

Result = Dict[str, Any]


def task_01(arg: str) -> Result:
    if not isinstance(arg, str):
        type_name = type(arg).__name__
        return {"errors": [f"type(arg)={type_name}, MUST be a string"]}

    rev = arg[::-1]
    return {"data": arg == rev}


def task_02() -> Result:
    return {"data": None}


def task_03() -> Result:
    return {"data": None}


def task_04() -> Result:
    return {"data": None}


def task_05() -> Result:
    return {"data": None}


def task_06() -> Result:
    return {"data": None}


def task_07() -> Result:
    return {"data": None}


def task_08() -> Result:
    return {"data": None}


def task_09() -> Result:
    return {"data": None}


def task_10() -> Result:
    return {"data": None}


def task_11() -> Result:
    return {"data": None}


def task_12() -> Result:
    return {"data": None}
