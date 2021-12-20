import math


def quadratic_equation() -> list:
    my_array = [[2, -5, 0], [2, 0, -3], [0, -5, 2]]
    result1 = []

    for i in range(len(my_array)):
        arg_a = my_array[i][0]
        arg_b = my_array[i][1]
        arg_c = my_array[i][2]
        discriminant = arg_b ** 2 - 4 * arg_a * arg_c

        if discriminant > 0 and arg_a != 0:
            x1 = (-arg_b + math.sqrt(discriminant)) / (2 * arg_a)
            x2 = (-arg_b - math.sqrt(discriminant)) / (2 * arg_a)
            result1.append([x1, x2])
        elif discriminant == 0:
            x3 = -arg_b / (2 * arg_a)
            result1.append([x3])
        else:
            x4 = bool(arg_a != 0)
            result1.append([x4])

    return result1
