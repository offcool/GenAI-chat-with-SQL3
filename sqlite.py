import sqlite3

try:
    #connect
    connection = sqlite3.connect("student.db")
    print("Database connection established.")
except sqlite3.Error as e:
    print(f"Error connecting to database: {e}")
    connection = None

if connection is not None:
    try:
        cursor = connection.cursor()
        print("Cursor created.")
    except sqlite3.Error as e:
        print(f"Error creating cursor: {e}")
        cursor = None
else:
    cursor = None


if cursor is not None:
    try:
        table_info = "create table STUDENT(NAME SEMEH(25),CLASS SEMEH(25),SECTION SEMEH(25) , MARKS INT) ;"
        cursor.execute(table_info)
        print("Table created or already exists.")
    except sqlite3.Error as e:
        print(f"Error executing SQL command: {e}")

cursor.execute('''Insert Into STUDENT values('Krish','Data Science','A',90)''')
cursor.execute('''Insert Into STUDENT values('John','Data Science','B',100)''')
cursor.execute('''Insert Into STUDENT values('Mukesh','Data Science','A',86)''')
cursor.execute('''Insert Into STUDENT values('Jacob','DEVOPS','A',50)''')
cursor.execute('''Insert Into STUDENT values('Dipesh','DEVOPS','A',35)''')


print("records are : ")
data = cursor.execute(''' select *from STUDENT ''')
for row in data:
    print (row)

connection.commit()
connection.close()