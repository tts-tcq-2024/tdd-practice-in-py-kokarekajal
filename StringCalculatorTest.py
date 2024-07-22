import unittest
from your_module_name import StringCalculator  # Update with the actual module name

class TestStringCalculator(unittest.TestCase):

    def test_expectZeroForEmptyInput(self):
        self.assertEqual(StringCalculator.add(""), 0)
    
    def test_expectZeroForSingleZero(self):
        self.assertEqual(StringCalculator.add("0"), 0)
        
    def test_expectSumForTwoNumbers(self):
        self.assertEqual(StringCalculator.add("1,2"), 3)
        
    def test_ignoreNumbersGreaterThan1000(self):
        self.assertEqual(StringCalculator.add("1,1001"), 1)
        
    def test_expectSumWithCustomDelimiter(self):
        self.assertEqual(StringCalculator.add("//;\n1;2"), 3)
        
    def test_expectSumWithNewlineDelimiter(self):
        self.assertEqual(StringCalculator.add("1\n2,3"), 6)

if __name__ == '__main__':
    unittest.main()
