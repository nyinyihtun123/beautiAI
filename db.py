import mysql.connector

def get_db_connection():
    return mysql.connector.connect(
        host='localhost',
        user='YOUR_DB_USER',
        password='YOUR_DB_PASSWORD',
        database='YOUR_DB_NAME'
    )
