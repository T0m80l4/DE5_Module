import unittest
from Docker_Demo.calculator_app import Calculator

class TestOperations(unittest.TestCase):
    
    def setUp(self):
        self.calc = Calculator(100,2)
    
    def test_sum(self):
        self.assertEqual(self.calc.get_sum(), 102, "The answer is wrong")

if __name__ == "__main__":
    unittest.main()