import unittest
import pandas as pd
from datetime import datetime

def calculate_loan_duration(book_data):
    """ Function to calculate loan duration in days for a DataFrame """
    book_data['Loan Duration (Days)'] = (book_data['Book Returned'] - book_data['Book checkout']).dt.days
    return book_data

class TestLoanDurationCalculation(unittest.TestCase):
    
    def setUp(self):
        """ Set up test data with known values """
        # Sample book data with checkout and return dates
        data = {
            'Books': ['Book 1', 'Book 2', 'Book 3'],
            'Book checkout': [datetime(2023, 2, 20), datetime(2023, 3, 24), datetime(2023, 3, 29)],
            'Book Returned': [datetime(2023, 2, 25), datetime(2023, 3, 21), datetime(2023, 3, 25)],
        }
        
        # Create DataFrame
        self.book_data = pd.DataFrame(data)
    
    def test_loan_duration(self):
        """ Test the loan duration calculation """
        # Apply the loan duration calculation function
        result = calculate_loan_duration(self.book_data)

        # Expected values for loan duration in days
        expected_durations = [5, -3, -4]

        # Test if the calculated loan durations match the expected durations
        for i in range(len(result)):
            self.assertEqual(result['Loan Duration (Days)'][i], expected_durations[i], f"Failed for Book: {result['Books'][i]}")

if __name__ == "__main__":
    unittest.main()
