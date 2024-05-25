import mysql.connector

# Connect to the database
connection = mysql.connector.connect(
    host="localhost",  # Your host, usually localhost
    user="matt",       # Your username
    password="password",       # Your password
    database="finalproject"  # Your database name
)

# Check if the connection was successful
if connection.is_connected():
    print("Connected to the database")
else:
    print("Failed to connect to the database")
