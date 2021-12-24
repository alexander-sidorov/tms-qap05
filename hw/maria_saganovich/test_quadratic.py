import unittest
from typing import Any
from unittest.mock import patch

from hw.maria_saganovich.quadratic_equation import quadratic_equation


class TestQuadraticEquation(unittest.TestCase):
    @patch("builtins.input", side_effect=[1, 2, 1])
    def test_quadratic_one_root(self, mock_input: Any) -> None:
        result = quadratic_equation()
        self.assertEqual(result, -1.0)

    @patch("builtins.input", side_effect=[1, 2, -5])
    def test_quadratic_two_roots(self, mock_input: Any) -> None:
        result = quadratic_equation()
        self.assertEqual(result, [1.4494897427831779, -3.449489742783178])

    @patch("builtins.input", side_effect=[0, 2, -5])
    def test_quadratic_no_roots(self, mock_input: Any) -> None:
        result = quadratic_equation()
        self.assertEqual(result, "'a' couldn't be = 0")
