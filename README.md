# MySQL_Python

Date: 14 MARCH 2022

The “Library Billing System” is a simple, user-friendly, menu driven Python program
that is designed to methodize the work of librarian or employees of
a library. The following functions are offered by the same:

1) To add and delete a book from the database
2) To modify the database and display the books in store
3) To perform or refer to a transaction
4) To show the transaction record of a book
5) To display genre popularity based on sales
6) To rank books based on total sales


It makes use of the python-MySQL connectivity. Tables are created
at the back end in SQL and the front end consists of functions in
Python. The main tables used to perform all operations are:

i. Main table of BOOKS
ii. TRANSACTIONS table
iii. NET table

When the program is executed, the Main Menu displays all possible
functions that can currently be performed by the program. On
entering suitable input, the corresponding output is displayed in
command prompt itself.
All data is stored in the MySQL database in the form of relations.
This simple program requires the tables to be created manually in the SQL server beforehand.

Menu Details and Options:

The main program menu is divided into 10 parts as follows with
multiple options under it:

1. ADD BOOK
▪ Add a Book ID for the book
▪ Add Book Name
▪ Add Book Genre
▪ Add rate of borrowing per week

2. DELETE BOOK
▪ Enter Book ID to delete book and associated records

3. MODIFY BOOK
▪ Enter Book ID to modify the records
▪ Update rent per week
▪ Update book genre

4. SHOW BOOKS
▪ Displays entire Book database

5. PERFORM A TRANSACTION
▪ Enter Book ID to display Book Name and Rate per Week
▪ Enter number of weeks to be rented for
▪ Receive total price and Transaction ID with completion message



6. REFER A TRANSACTION
▪ Enter Transaction ID to display transaction details including
Book ID, Book Name, Sales Amount, Date & Time of transaction
7. SHOW TRANSACTION RECORDS OF A BOOK
▪ Enter Book ID to display Transaction History of book

8. SHOW GENRE POPULARITY BASED ON SALES
▪ Displays entire Book database ranked in terms of Genre
Popularity

9. RANK BOOKS BASED ON TOTAL SALES
▪ Displays entire Book database ranked in terms of Total Sales

10. EXIT PROGRAM

Concepts used:
1. User defined functions
2. Built-In functions
3. Python-SQL connectivity
4. Other libraries and modules (Random, tabulate)

Requirements: • Python 3.7 or higher , • MySQL 8.0 or higher
