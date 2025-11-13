import unittest
import pandas as pd
from datetime import datetime
from DE5_DataCleanse_Modular import convert_days_allowed, calculate_loan_duration, clean_book_data, clean_customer_data

class TestDataCleansing(unittest.TestCase):

    def setUp(self):
        """ Set up test data with known values """
        # Sample book data with checkout and return dates
        data = {
            'Books': ['Book 1', 'Book 2', 'Book 3'],
            'Book checkout': [datetime(2023, 2, 20), datetime(2023, 3, 24), datetime(2023, 3, 29)],
            'Book Returned': [datetime(2023, 2, 25), datetime(2023, 3, 21), datetime(2023, 3, 25)],
            'Days allowed to borrow': ['2 weeks', '10 days', '3 weeks']
        }
        # Create DataFrame
        self.book_data = pd.DataFrame(data)

        # Sample customer data
        customer_data = {
            'Customer ID': [1, 2, 3, 4],
            'Customer Name': ['Alice', 'Bob', None, 'David']
        }
        self.customer_data = pd.DataFrame(customer_data)

    def test_convert_days_allowed(self):
        """ Test the conversion of 'Days allowed to borrow' """
        # Test with '2 weeks'
        self.assertEqual(convert_days_allowed('2 weeks'), 14)

        # Test with '10 days'
        self.assertEqual(convert_days_allowed('10 days'), 10)

        # Test with invalid unit
        self.assertIsNone(convert_days_allowed('3 months'))

    def test_calculate_loan_duration(self):
        """ Test the loan duration calculation """
        # Apply the loan duration calculation function
        result = calculate_loan_duration(self.book_data)

        # Expected values for loan duration in days
        expected_durations = [5, -3, -4]

        # Test if the calculated loan durations match the expected durations
        for i in range(len(result)):
            self.assertEqual(result['Loan Duration (Days)'][i], expected_durations[i], f"Failed for Book: {result['Books'][i]}")

    def test_clean_book_data(self):
        """ Test the cleaning of book data """
        # Apply the cleaning function
        result = clean_book_data(self.book_data)

        # Check if the loan durations were correctly calculated and negative durations were set to None
        self.assertIsNone(result['Loan Duration (Days)'][1])  # Book 2: Invalid duration
        self.assertIsNone(result['Loan Duration (Days)'][2])  # Book 3: Invalid duration
        self.assertEqual(result['Days allowed to borrow'][0], 14)  # Book 1: 2 weeks = 14 days

if __name__ == "__main__":
    unittest.main()
