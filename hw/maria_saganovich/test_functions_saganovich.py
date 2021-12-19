def a():
    num1 = 1
    if num1 % 2 == 0:
        return True
    else:
        return False


print(a())


def b():
    num2 = 8
    if num2 % 2 == 0:
        return True
    else:
        return False


print(b())


def c():
    return


print(c())


def f():
    for i in range(-10, 10):
        if i < 0:
            print(i)
        else:
            print("i >= 0")
            break


print(f())
