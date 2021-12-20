import math


def quadratic_equation():
    print("Enter the coefficients for the equation: ")

    print("ax^2 + bx + c = 0:")
    a1 = check_user_input("a")

    while a1 == 0:
        print("'a' couldn't be = 0")
        a1 = check_user_input("a")

    b1 = check_user_input("b")
    c1 = check_user_input("c")

    discriminant = b1 ** 2 - 4 * a1 * c1
    print("Discriminant:\nD = %.1f" % discriminant)  # noqa: S001

    if discriminant > 0:
        x1 = (-b1 + math.sqrt(discriminant)) / (2 * a1)
        x2 = (-b1 - math.sqrt(discriminant)) / (2 * a1)
        print(
            "We have the next roots: \nx1 = %.1f \nx2 = %.1f"
            % (x1, x2)  # noqa: S001
        )

    elif discriminant == 0:
        x3 = -b1 / (2 * a1)
        print("We have the next root:\nx = %.1f" % x3)  # noqa: S001

    else:
        print("We have the next roots: \nNo roots")

    print("Recalculate the equation? Enter your answer: y/n")

    res = str(input("Answer: ").lower())
    if res == "y":
        return quadratic_equation()
    else:
        print("See you next time.")
        return True


def check_user_input(name):
    while True:
        val1 = input(name + " = ")
        try:
            val1 = int(val1)
            break
        except ValueError:
            try:
                return float(val1)
            except ValueError:
                print("Value couldn't be a string \nTry again")

                val1 = check_user_input(name)
                break
    return val1
