import sqlite3

# function for create database and table
def create():
    # create connection by using object to connect with database
    connection = sqlite3.connect("database.db")

    # create a table in database
    connection.execute('''CREATE TABLE IF NOT EXISTS students(
                    student_id INT PRIMARY KEY,
                    student_name TEXT NOT NULL,
                    age INT NOT NULL,
                    dob TEXT NOT NULL)''')
    print("Table created")

#add one record into table
def insert_data(id,name,age,dob):
    connection=sqlite3.connect("database.db")
    cursor=connection.cursor()
    query='INSERT INTO students VALUES(?,?,?,?)'
    cursor.execute(query,(id,name,age,dob))
    connection.commit()
    print("Record inserted")
    connection.close()

# retrieve all rows from the students table
def showall():
    connection=sqlite3.connect("database.db")
    cursor=connection.cursor()
    cursor.execute("SELECT * FROM students")
    items=cursor.fetchall()
    print("students table")
    for item in items:
        print(item)

# insert multiple records into students table
def insert_manyrecords(list):
    connection=sqlite3.connect("database.db")
    cursor=connection.cursor()
    query=("INSERT INTO students VALUES (?,?,?,?)")
    cursor.executemany(query,list)
    connection.commit()
    print("Many records added")
    connection.close()

#update record
def update_record(*,id):
    connection=sqlite3.connect("database.db")
    cursor=connection.cursor()
    query="UPDATE students SET student_name='manoj kumar' WHERE student_id=(?)"
    cursor.execute(query,(id,))
    connection.commit()
    print("Updated the record")
    connection.close()

#Delete record function
def delete_record(id,/):
    connection=sqlite3.connect("database.db")
    cursor=connection.cursor()
    query="DELETE FROM students WHERE student_id=(?)"
    cursor.execute(query,(id,))
    connection.commit()
    print("Deleted record")
    connection.close()

# order by function
def order_record():
    connection=sqlite3.connect("database.db")
    cursor=connection.cursor()
    query='SELECT * FROM students ORDER BY student_name'
    cursor.execute(query)
    rows=cursor.fetchall()
    print("Order by student name")
    for row in rows:
        print(row)
    connection.close()

#Truncate all records in table
def truncate_records():
    connection=sqlite3.connect("database.db")
    cursor=connection.cursor()
    query='DELETE FROM students'
    cursor.execute(query)
    connection.commit()
    print("Deleted all rows")
    connection.close()

# AND/OR
def like_record():
    connection=sqlite3.connect("database.db")
    cursor=connection.cursor()
    query='SELECT * FROM students WHERE student_name LIKE "ud%" AND age=15'
    cursor.execute(query)
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    connection.commit()
    connection.close()

#DELETE table from the database
def drop_table():
    connection=sqlite3.connect("database.db")
    cursor=connection.cursor()
    query="DROP TABLE students"
    cursor.execute(query)
    connection.commit()
    print("TABLE DELETED")
    connection.close()