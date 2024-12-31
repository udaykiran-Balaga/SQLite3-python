# SQLite Operations with Python

This project demonstrates various SQLite database operations using Python. It includes functions to perform CRUD (Create, Read, Update, Delete) operations and search queries on a `students` table.

## Features

- **Insert Records**: Add new student records to the database.
- **Update Records**: Modify existing student information.
- **Delete Records**: Remove specific records from the database.
- **Retrieve Records**: Fetch records with sorting and filtering.
- **Search with LIKE**: Search for students based on partial name matches and specific conditions.

## Table Schema

The `students` table used in this project has the following structure:

| Column        | Type        | Description                      |
|---------------|-------------|----------------------------------|
| `student_id`  | INTEGER     | Unique identifier for each student |
| `student_name`| TEXT        | Name of the student             |
| `age`         | INTEGER     | Age of the student              |
| `dob`         | TEXT        | Date of birth (in `DD/MM/YYYY` format) |


## Working with SQLite in Visual Studio Code (VS Code)
To handle SQLite databases conveniently, you can use the SQLite extension for VS Code.

Setting Up SQLite in VS Code
Install SQLite Extension:

Go to the Extensions Marketplace in VS Code.
Search for "SQLite" and install a popular extension like SQLite Viewer or SQLite Explorer.
Open Your SQLite Database:

Right-click on your database.db file in the VS Code Explorer panel.
Select the option to "Open in SQLite Explorer" or similar, depending on the extension.
Run Queries:

Use the SQLite extension’s built-in query editor to run SQL queries.
View and modify your students table directly from VS Code.
Debugging Python SQLite Code:

Use the VS Code terminal to run your Python scripts and see the output of your SQLite operations.
Example:
bash
Copy code
python your_script_name.py
Visualize Tables:

With the SQLite extension, you can easily visualize tables, view schema details, and manage records without leaving VS Code.

## Using the SQLite Module in Python
The project includes a sqlite.py file that defines various database operations. You can import this module into your Python scripts to perform database tasks efficiently.

### Importing the Module

To use the module, follow these steps:

Ensure the sqlite.py file is in the same directory as your main script or is accessible in your Python path.
Import the module using the import statement.
