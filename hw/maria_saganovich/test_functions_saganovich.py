

def a():
    num1 = 1
    if num1 % 2 == 0:
        return True
    else:
        return False


a()


def b():
    num2 = 8
    if num2 % 2 == 0:
        return True
    else:
        return False


b()


def c():
    return


c()


def f():
    array1 = [-5, 3, 20, 0, -99]
    x = 0
    result = []
    for number in array1:
        if number < x:
            result.append(number)
    return result


f()


def e():
    array2 = ["Seoul", "Jeju", "Oslo", '']
    result2 = []
    for word in array2:
        if word == '':
            result2.append(word)
    return result2


e()
