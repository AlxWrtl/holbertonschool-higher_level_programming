#!/usr/bin/python3
"""
Module for database interaction example.

This script demonstrates a simple usage of MySQLdb for interacting with a
MySQL database. It connects to the database, retrieves data from the 'states'
table, and prints each row. It utilizes command-line arguments for database
authentication and selection.
"""

import MySQLdb
from sys import argv

if __name__ == '__main__':
    """
    Connect to the MySQL database using credentials and database name
    provided as command-line arguments.
    """
    db = MySQLdb.connect(
        host="localhost",  # Database host
        user=argv[1],      # Username from command-line argument
        port=3306,         # Default MySQL port
        passwd=argv[2],    # Password from command-line argument
        db=argv[3]         # Database name from command-line argument
    )

    # Create a cursor object to interact with the database
    cur = db.cursor()

    """
    Execute a SQL query to select all rows from the 'states' table and
    order them by 'id' in ascending order.
    """
    cur.execute("SELECT * FROM states ORDER BY id ASC")

    # Fetch all the rows returned by the executed query.
    rows = cur.fetchall()

    # Iterate over the rows and print each one.
    for row in rows:
        print(row)

    # Close the cursor and database connection.
    cur.close()
    db.close()
