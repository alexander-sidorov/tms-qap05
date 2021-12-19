import math


class colors:
    BLUE = '\033[94m'
    End_of_work = '\033[93m'
    ERROR = '\033[91m'
    END = '\033[0m'
    BOLD = '\033[1m'


def quadratic_equation():
    print(colors.BLUE + "Enter the coefficients for the equation: " + colors.END)
    print(colors.BOLD + "ax^2 + bx + c = 0:" + colors.END)
    a = check_user_input('a')

    while a == 0:
        print(colors.ERROR + "'a' couldn't be = 0" + colors.END)
        a = check_user_input('a')

    b = check_user_input('b')
    c = check_user_input('c')

    discriminant = b ** 2 - 4 * a * c
    print(colors.BLUE + "Discriminant:\n" + colors.END + "D = %.1f" % discriminant)

    if discriminant > 0:
        x1 = (-b + math.sqrt(discriminant)) / (2 * a)
        x2 = (-b - math.sqrt(discriminant)) / (2 * a)
        print(colors.BLUE + "We have the next roots: \n" + colors.END + "x1 = %.1f \nx2 = %.1f" % (x1, x2))
    elif discriminant == 0:
        x = -b / (2 * a)
        print(colors.BLUE + "We have the next root:\nx = %.1f" % x + colors.END)
    else:
        print(colors.BLUE + "We have the next roots: \n" + colors.END + colors.ERROR + "No roots" + colors.END)

    print(colors.BLUE + "Do you want to recalculate the equation? Enter you answer: " + colors.END + "y/n")
    r = str(input(colors.BLUE + "Answer: " + colors.END))
    if r == "y":
        return quadratic_equation()
    else:
        print(colors.End_of_work + "See you next time." + colors.END)
        return True


def check_user_input(name):
    while True:
        val = input(name + ' = ')
        try:
            val = int(val)
            break
        except ValueError:
            try:
                return float(val)
            except ValueError:
                print(colors.ERROR + "Value couldn't be a string \n" + colors.END
                      + colors.BLUE + "Try again: " + colors.END)
                val = check_user_input(name)
                break
    return val


quadratic_equation()
