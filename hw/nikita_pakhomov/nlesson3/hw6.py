def is_palindrome(text: str):
    result = {}
    s1 = "".join(c for c in text if c.isalpha())
    a = s1.lower()
    reverst_a = a[::-1]
    result["data"] = reverst_a == a
    return result
