"""Script to create a database to the mysql server"""

from mysql.connector import connect, Error

try:
    conn = connect(host='localhost', user='root',
                        password='Arp@99?0#1Liy@')
    if conn.is_connected():
        cursor = conn.cursor()
        cursor.execute("CREATE DATABASE testdb")
        print("Database is created")
except Error as e:
    print("Error while connecting to MySQL", e)
