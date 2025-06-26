import mysql.connector
from mysql.connector import Error

# connect to database
try:
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Mohamed112015"
    )

    # create cursor if connect
    if mydb.is_connected():
        print("Connected")
        cursor = mydb.cursor()

    # create database
    try:
        cursor.execute("CREATE DATABASE alx_book_store")
        print("Database 'alx_book_store' created successfully!")
    except Error as err:
        if err.errno == 1007:  # ER_DB_CREATE_EXISTS
            print("Database 'alx_book_store' already exists.")
        else:
            print(f"Failed creating database: {Error}")  

except Error as err:
    print(f"Connection Error : {err}")

finally:
    try:
        if cursor:
            cursor.close()
        if mydb.is_connected():
            mydb.close()
            print("Connection closed.")
    except NameError:
        # cursor may not be defined if connection fails early
        print(NameError)


