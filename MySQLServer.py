import mysql.connector
from mysql.connector import Error


def create_database():
    try:
        # Connect to MySQL Server 
        connection = mysql.connector.connect(
            host="localhost", 
            user="root", 
            password="*****",  
            auth_plugin='mysql_native_password'
        )

        if connection.is_connected():
            cursor = connection.cursor()

            # Create database if it doesn't exist and show appropriate message
            cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store;")
            
            print("Database 'alx_book_store' created successfully!")

    except Error as e:
        print(f"Error: Could not connect to MySQL Server - {e}")

    finally:
        # Close cursor and connection
        if "cursor" in locals():
            cursor.close()
        if "connection" in locals() and connection.is_connected():
            connection.close()
            print("MySQL connection closed.")


create_database()
