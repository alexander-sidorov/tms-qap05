def is_palindrome(text: str) -> dict:
    result = {}
    s1 = "".join(c for c in text if c.isalpha())
    abc = s1.lower()
    reverst_a = abc[::-1]
    result["data"] = reverst_a == abc
    return result
