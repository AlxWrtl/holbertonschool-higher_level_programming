#!/usr/bin/python3
"""
Module for filtering states from a database based on a given name.

This script filters states from the 'hbtn_0e_0_usa' database whose names match
a specific argument (case sensitive). It utilizes MySQLdb for database
connection and querying, incorporating command-line arguments for database
credentials and the name to filter by.
"""

import MySQLdb
from sys import argv

if __name__ == '__main__':
    """
    Connect to the MySQL database using credentials and database name
    provided as command-line arguments. Retrieves states matching a
    specific name.
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
    Execute a SQL query to select states matching a specific name
    provided as a command-line argument.
    """
    cur.execute(
        "SELECT * FROM states WHERE name LIKE BINARY '{}' ORDER BY \
            states.id ASC".format(argv[4])
    )

    # Fetch and print all rows that match the query
    rows = cur.fetchall()
    for row in rows:
        print(row)

    # Close the cursor and database connection
    cur.close()
    db.close()
