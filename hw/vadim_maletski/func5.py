def level1(p1: list) -> tuple:
    p2 = (p1[0], p1[-1])
    return p2


def level2(p1: str) -> str:
    p2 = p1.split()
    p2.reverse()
    p3 = " ".join(p2)
    return p3


def level3(p1: list, p2: int) -> list:
    index = p1.index(p2)
    p3 = p1[0 : (index + 1)]  # noqa: E203
    return p3


def level4(p1: str, p2: str) -> str:
    p3 = list(p1)
    p4 = p2.join(p3)
    return p4


def level5(p1: str) -> str:
    p2 = " ".join(p1.split())
    p3 = p2.title()
    return p3


def level6(plaintext: str, key: str, alphabet: str) -> str:
    num = len(plaintext)
    text = []
    i = 0
    while i < num:
        words = alphabet[key.index(str(plaintext[i]))]
        text.append(words)
        i += 1
    return "".join(text)
