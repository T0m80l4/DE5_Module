import pandas as pd
from datetime import datetime
import os

def convert_days_allowed(value):
    """ Convert 'Days allowed to borrow' from weeks (e.g., '2 weeks') to numeric days """
    if isinstance(value, str):
        value = value.strip().lower()
        if 'week' in value:
            # Extract the numeric part and convert weeks to days (multiply by 7)
            return int(value.split()[0]) * 7
        elif 'day' in value:
            # If it's already in days, just extract the number
            return int(value.split()[0])
        else:
            # If the unit is unrecognized, return NaN (can be handled further if needed)
            return None
    return value

def calculate_loan_duration(book_data):
    """ Calculate loan duration in days for a DataFrame """
    book_data['Loan Duration (Days)'] = (book_data['Book Returned'] - book_data['Book checkout']).dt.days
    return book_data

def clean_book_data(book_file_path, book_error_file_path):
    """ Clean the book data by calculating loan duration and converting 'Days allowed to borrow' to days """
    
    # Load the book data
    book_data = pd.read_csv(book_file_path)

    # Convert 'Book checkout' and 'Book Returned' columns to datetime, handle invalid formats
    book_data['Book checkout'] = pd.to_datetime(book_data['Book checkout'].str.replace('"', ''), errors='coerce')
    book_data['Book Returned'] = pd.to_datetime(book_data['Book Returned'].str.replace('"', ''), errors='coerce')

    # Calculate loan duration in days
    book_data = calculate_loan_duration(book_data)

    # Handle negative loan durations (set to NaN for further review)
    book_data['Loan Duration (Days)'] = book_data['Loan Duration (Days)'].apply(lambda x: x if x >= 0 else None)

    # Convert 'Days allowed to borrow' to numeric days
    book_data['Days allowed to borrow'] = book_data['Days allowed to borrow'].apply(convert_days_allowed)

    return book_data

def clean_customer_data(customer_file_path, customer_error_file_path):

    # Load the customer data
    customer_data = pd.read_csv(customer_file_path)

    # Identify rows with missing customer data (Customer ID or Customer Name)
    customer_errors = customer_data[customer_data['Customer ID'].isnull() | customer_data['Customer Name'].isnull()]

    # Save the error rows to a separate CSV file for manual review
    if not customer_errors.empty:
        customer_errors.to_csv(customer_error_file_path, index=False)
        print(f"Found errors in customer data. {len(customer_errors)} rows saved to {customer_error_file_path}.")

    # Remove error rows from the cleaned data
    customer_data_cleaned = customer_data.dropna(subset=['Customer ID', 'Customer Name'])

    return customer_data_cleaned

def main():
    # Define file paths
    book_file_path = r'C:\Users\Admin\Desktop\DE5_Module\03_Library_Systembook.csv'
    customer_file_path = r'C:\Users\Admin\Desktop\DE5_Module\03_Library_SystemCustomers.csv'
    book_error_file_path = 'book_data_errors.csv'  # File to store book data errors
    customer_error_file_path = 'customer_data_errors.csv'  # File to store customer data errors

    # Check the current working directory
    print(f"Current working directory: {os.getcwd()}")

    # Clean the data
    cleaned_book_data = clean_book_data(book_file_path, book_error_file_path)
    cleaned_customer_data = clean_customer_data(customer_file_path, customer_error_file_path)

    # Save cleaned data to new CSV files
    cleaned_book_data.to_csv('cleaned_books_data.csv', index=False)
    cleaned_customer_data.to_csv('cleaned_customers_data.csv', index=False)

    print("Data cleaning complete. Cleaned data saved to 'cleaned_books_data.csv' and 'cleaned_customers_data.csv'.")

if __name__ == "__main__":
    main()