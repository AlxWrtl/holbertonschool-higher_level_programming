#!/usr/bin/python3
"""
Module for filtering states from a database.

This script filters states from the database 'hbtn_0e_0_usa' whose names start
with 'N' (case sensitive) and lists them. It demonstrates the use of MySQLdb
for database connection and querying with command-line arguments for database
access credentials and filtering criteria.
"""

import MySQLdb
from sys import argv

if __name__ == '__main__':
    """
    Connect to the MySQL database using credentials and database name
    provided as command-line arguments.
    """
    db = MySQLdb.connect(
        host="localhost",  # Database server address
        user=argv[1],      # Database username
        port=3306,         # Database server port
        passwd=argv[2],    # Database password
        db=argv[3]         # Database name
    )

    # Create a cursor object to execute SQL queries
    cur = db.cursor()

    """
    Execute a SQL query to select states starting with 'N'
    """
    cur.execute(
        "SELECT * FROM states WHERE name LIKE BINARY\
            'N%' ORDER BY states.id ASC"
    )

    # Fetch and print all rows that match the query
    rows = cur.fetchall()
    for row in rows:
        print(row)

    # Close the cursor and database connection
    cur.close()
    db.close()
