from hw.alexander_sidorov.lesson06.common import Result


def task_01(arg: str) -> Result:
    """
    Tells if the arg is a palindrome
    """

    if not isinstance(arg, str):
        type_name = type(arg).__name__
        return {"errors": [f"type(arg)={type_name}, MUST be a string"]}

    rev = arg[::-1]
    return {"data": arg == rev}
