import sqlite3

# create a connection to a new database (if the database does not exist then it will be created).
db = sqlite3.connect("books-collection.db")

# we need to create a cursor ("mouse" or "pointer") which will control our database
# If we were working in Excel or Google Sheet, we would be using the cursor to add rows of data or edit/delete data, we also need a cursor to modify our SQLite database.
cursor = db.cursor()

# single Excel file can contain many tables (sheets- this rectangle at the bottom), each tab is a different table.
# Similarly, our database can contain many tables.
cursor.execute("CREATE TABLE books ("
               "id INTEGER PRIMARY KEY, "
               "title varchar(250) NOT NULL UNIQUE, "
               "author varchar(250) NOT NULL, "
               "rating FLOAT NOT NULL)")
# .execute() <- This method will tell the cursor to execute an action.
# CREATE TABLE books <- SQL command of creating new table named "books"
# what is in the parenthesis tell about "columns" and they type:
    # id INTEGER PRIMARY KEY <- id it's name, Integer is type, Primaty key <- this kolumn will be primary key for this table - The primary key is the one piece of data that will uniquely identify
    # title varchar(250) NOT NULL UNIQUE <-
        # title is name, varchar(250) means string type of max length 250,
        # NOT NULL means that cant be empty, and UNIQUE means that there cannot be 2 or more same records
