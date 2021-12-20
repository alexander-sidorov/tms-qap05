from for_input_auto_test import get_display_output
from for_input_auto_test import set_keyboard_input
from quadratic_equation import quadratic_equation


def test1():
    set_keyboard_input([1, 2, -5, "n"])

    quadratic_equation()

    output = get_display_output()

    assert output == [
        "\x1b[94mEnter the coefficients for the equation: \x1b[0m",
        "\x1b[1max^2 + bx + c = 0:\x1b[0m",
        "a = ",
        "b = ",
        "c = ",
        "\x1b[94mDiscriminant:\n" "\x1b[0mD = 24.0",
        "\x1b[94mWe have the next roots: \n" "\x1b[0mx1 = 1.4 \n" "x2 = -3.4",
        "\x1b[94mDo you want to recalculate the equation? Enter you answer: "
        "\x1b[0my/n",
        "\x1b[94mAnswer: \x1b[0m",
        "\x1b[93mSee you next time.\x1b[0m",
    ]
