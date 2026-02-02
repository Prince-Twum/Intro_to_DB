import mysql.connector
from mysql.connector import Error

def create_database():
    try:
        # Connect to MySQL Server
        db_connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="123456789"  # <--- REPLACE THIS
        )

        cursor = db_connection.cursor()

        # Create Database
        cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
        print("Database 'alx_book_store' created successfully!")

    except mysql.connector.Error as err:
        print(f"Failed to connect to MySQL server: {err}")

    finally:
        # Close connection
        if 'db_connection' in locals() and db_connection.is_connected():
            cursor.close()
            db_connection.close()
            print("MySQL connection is closed")

if __name__ == "__main__":
    create_database()
