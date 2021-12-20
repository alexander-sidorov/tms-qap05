def a():
    return True


def b():
    return False


def c():
    return None


def d():
    return -1


def e():
    return ""


def solve(a, b, c):
    from math import sqrt, pow, pi, floor, ceil

    d = (b ** 2) - 4 * a * c

    if d < 0:
        return "Нет корней"
    elif d == 0:
        v = -b / (2 * a)
        return v, v
    else:
        x1 = ((-b) - (sqrt(d))) / (2 * a)
        x2 = ((-b) + (sqrt(d))) / (2 * a)

        return (min(x1, x2)), (max(x1, x2))
