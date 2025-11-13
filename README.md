# DE5_Module

Author: Thomas Wilkinson

Brief: 

Build a Library Application that takes cutomer & book hire data from input files, cleanses / enriches the data and then writes to a datastore.

Solution:

Python application that reads .csv input files and writes to a SQL Database

Data Cleansing Functions:
Convert strings to dates
Return maximum permissable rental period in days
Remove missing data (NaN values)
Normalise Book Titles (Fix capitalisation errors, strip whitespace)
Return rental duration
Identify incorrect data

Error Handling:
Rows with NaN Values
Rows where book checkout > book returned date
Rows with invalid dates

