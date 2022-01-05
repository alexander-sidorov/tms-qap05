from typing import Any


new_type = Dict[str, Any]
def polindrom(stroka: Any) -> new_type:
    result = {}

    if type(stroka) != str:
        result["errors"] = ["this is not a string"]
    else:
        if stroka == stroka[::-1]:
            result["data"] = True
        else:
            result["data"] = False
    return result
