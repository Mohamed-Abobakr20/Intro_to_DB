import mysql.connector

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

        # create database
        try:
            cursor = mydb.cursor()
            cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
            print("Database 'alx_book_store' created successfully!")
        except mysql.connector.Error as err:
            print(f"Failed creating database: {err}")  

# handle connection error
except mysql.connector.Error as err:
    print(f"Connection Error : {err}")

# close database connection
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


