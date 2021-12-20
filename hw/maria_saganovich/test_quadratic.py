from hw.maria_saganovich.for_input_auto_test import get_display_output, set_keyboard_input
from hw.maria_saganovich.quadratic_equation import quadratic_equation


def test1():
    set_keyboard_input([1, 2, -5, "n"])

    quadratic_equation()

    output = get_display_output()

    assert output == [
        "Enter the coefficients for the equation: ",
        "ax^2 + bx + c = 0:",
        "a = ",
        "b = ",
        "c = ",
        "Discriminant: D = 24.0",
        "We got the next roots: x1 = 1.4, x2 = -3.4",
        "Recalculate the equation? Enter your answer: y/n",
        "Answer: ",
        "See you next time.",
    ]
