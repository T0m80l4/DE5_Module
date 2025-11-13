SELECT [Books],
		CASE
			WHEN [Loan Duration (Days)] <= 14 THEN 'ON TIME'
			WHEN [Loan Duration (Days)] > 14 THEN 'OVERDUE'
		END AS [Loan Duration]
FROM [LibraryDB].[dbo].[STAGE.Books_Data]

SELECT Books
	FROM [LibraryDB].[dbo].[STAGE.Books_Data]
	WHERE [Loan Duration (Days)] <= 14

SELECT Books
	FROM [LibraryDB].[dbo].[STAGE.Books_Data]
	WHERE [Loan Duration (Days)] > 14

SELECT COUNT (*)
	FROM [LibraryDB].[dbo].[STAGE.Books_Data]

SELECT COUNT (*)
	FROM [LibraryDB].[dbo].[ERRORS.Book_Data]