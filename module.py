import sqlite # sqlite.py => module name

#call the function to create database and table
sqlite.create()

#call function to insert one record
sqlite.insert_data(1,'uday',15,"7/8/2009")

data=[
    (2,'kiran',15,"5/12/2009"),
    (3,'jyostna',15,"8/1/2009"),
    (4,'manoj',15,"18/6/2009"),
    (5,'udaykiran',15,"7/8/2009")
]
# call the function to insert multiple records into table
sqlite.insert_manyrecords(data)

#call the function to update record based on student id
sqlite.update_record(id=4)

#function call to orderby clause on student_name column
sqlite.order_record()

#invoke function to delete the record in the table
sqlite.delete_record(5)

#invoke function to delete all rows in the table
sqlite.truncate_records()
sqlite.showall() #invoke function to fetch all rows from the table

# This function invoke the condition of Like and AND/OR
sqlite.like_record()

# Drop the entire table from the database
#sqlite.drop_table()





