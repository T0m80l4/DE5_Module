import unittest
from Docker_Demo.calculator_app import Calculator

class TestOperations(unittest.TestCase):
    def test_sum(self):
        calc = Calculator(2, 8)
        self.assertEqual(calc.get_sum(), 10, "The sum is wrong")

    # Test: difference
    def test_diff(self):
        calc=Calculator(5, 1)
        self.assertEqual(calc.get_difference(), 4, "The sum is wrong")

    # Test: product
    def test_prod(self):
        calc=Calculator(2, 2)
        self.assertEqual(calc.get_product(), 4, "The sum is wrong")


if __name__ == "__main__":
    unittest.main()