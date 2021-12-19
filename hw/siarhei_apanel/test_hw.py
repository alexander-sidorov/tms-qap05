a1 = 1
back = 2
call = 1

def func(a1, back, call):
    if a1 == 0:
        return "Нет корней"
    disk = back ** 2 - 4 * a1 * call
    sqrt = disk ** (0.5)
    if disk > 0:
        x1 = (-back + sqrt) / 2 * a1
        x2 = (-back - sqrt) / 2 * a1
        return x1, x2
    elif disk == 0:
        xone = (-back + sqrt) / 2 * a1
        return xone
    else:
        return "Нет корней"

xs = 0
if xs == 0:
    xs == func(1, 2, 1)