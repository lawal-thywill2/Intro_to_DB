import mysql.connector

# Replace with your connection details
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Thywilll@123",
    database="alx_book_store"
)

mycursor = mydb.cursor()
mycursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
print("Database 'alx_book_store' created successfully!")
# Execute SQL statements using the execute() method on the cursor

# Close connection to the databasse  
mycursor.close()
mydb.close()