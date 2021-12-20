import math


class Colors:
    BLUE = "\033[94m"
    End_of_work = "\033[93m"
    ERROR = "\033[91m"
    END = "\033[0m"
    BOLD = "\033[1m"


def quadratic_equation():
    print(
        Colors.BLUE + "Enter the coefficients for the equation: " + Colors.END
    )
    print(Colors.BOLD + "ax^2 + bx + c = 0:" + Colors.END)
    a = check_user_input("a")

    while a == 0:
        print(Colors.ERROR + "'a' couldn't be = 0" + Colors.END)
        a = check_user_input("a")

    b = check_user_input("b")
    c = check_user_input("c")

    discriminant = b ** 2 - 4 * a * c
    print(
        Colors.BLUE
        + "Discriminant:\n"
        + Colors.END
        + "D = %.1f" % discriminant
    )

    if discriminant > 0:
        x1 = (-b + math.sqrt(discriminant)) / (2 * a)
        x2 = (-b - math.sqrt(discriminant)) / (2 * a)
        print(
            Colors.BLUE
            + "We have the next roots: \n"
            + Colors.END
            + "x1 = %.1f \nx2 = %.1f" % (x1, x2)
        )
    elif discriminant == 0:
        x = -b / (2 * a)
        print(
            Colors.BLUE + "We have the next root:\nx = %.1f" % x + Colors.END
        )
    else:
        print(
            Colors.BLUE
            + "We have the next roots: \n"
            + Colors.END
            + Colors.ERROR
            + "No roots"
            + Colors.END
        )

    print(
        Colors.BLUE
        + "Do you want to recalculate the equation? Enter you answer: "
        + Colors.END
        + "y/n"
    )
    r = str(input(Colors.BLUE + "Answer: " + Colors.END).lower())
    if r == "y":
        return quadratic_equation()
    else:
        print(Colors.End_of_work + "See you next time." + Colors.END)
        return True


def check_user_input(name):
    while True:
        val = input(name + " = ")
        try:
            val = int(val)
            break
        except ValueError:
            try:
                return float(val)
            except ValueError:
                print(
                    Colors.ERROR
                    + "Value couldn't be a string \n"
                    + Colors.END
                    + Colors.BLUE
                    + "Try again: "
                    + Colors.END
                )
                val = check_user_input(name)
                break
    return val


# if __name__ == "__main__":
#     quadratic_equation()
