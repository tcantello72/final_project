Cantello National Bank Project 

This project was created using Flask for the front end and Python for the backend. It contains a one table sqlite database. This was my first time using Flask to create a webpage
with Python running the back end. The project is very basic page a teller at a bank could use. 

The Minimum Viable Product (MVP) requirements for this project were:
1. Python running the back-end
2. Flask used to create the web interface for the project
3. Be able to use CRUD
   	a. Create a record in the database
   	b. Read records from the database
   	c. Update a record from the database
   	d. Delete a record from the database

Main Page
The main page is made of two tables. The first table allows a user Add an account to the database. The type of account is locked to a predetermined list of accounts (Checking, Savings,
CD, Home Loan and Car Loan). All the input files are set that they have to be filled in before the record can be added. If a user tries to Add an Account with an empty field they will 
see a flag next to the empty field reminding them to fill it out before submitting. The second table is dynamically created each time the page is loaded or a new account is added. From
this table a user can delete an account or click on the link to load the Update page.

Update Page
The update page is one table and allows the user to update any of the account information. Again the user will not be able to submit the record update with a null field. Once the account
is update it reloads the main page reflecting the changes made.

Future Upgrades:
Main Page:
	1. Add a second table to the database to record Customer Address, phone number, etc
	2. Be able to access the customer details by clicking on Last name
	3. Search by last name, email or account type to locate certian records and not all records
Update Page:
	1. Add fields for withdraw and deposit and does the calcuations to update the balance 
	2. Add the abilty to update the person information once that table is added to the database.


