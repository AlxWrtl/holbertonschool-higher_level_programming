#!/usr/bin/python3
"""
Module for safe filtering of states from a database.

This script filters states from the 'hbtn_0e_0_usa' database where the name
matches a given argument, employing parameterized queries to safeguard against
SQL injection. It demonstrates the use of MySQLdb for secure database
connection and querying, with command-line arguments for database credentials
and the filtering criteria.
"""

import MySQLdb
from sys import argv

if __name__ == '__main__':
    """
    Connect to the MySQL database using credentials and database name
    provided as command-line arguments. Retrieves states matching a
    specific name in a manner safe from SQL injection.
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
    Execute a SQL query using a parameterized statement to select states
    matching a specific name provided as a command-line argument, ensuring
    the query is safe from SQL injection.
    """
    cur.execute(
        "SELECT * FROM states WHERE name LIKE \
            BINARY %(name)s ORDER BY states.id ASC", {'name': argv[4]}
    )

    # Fetch and print all rows that match the query
    rows = cur.fetchall()
    for row in rows:
        print(row)

    # Close the cursor and database connection
    cur.close()
    db.close()
