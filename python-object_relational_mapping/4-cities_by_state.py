#!/usr/bin/python3
"""
Module for listing cities from a database.

This script lists all cities from the 'hbtn_0e_0_usa' database, joining them
with their corresponding states. It demonstrates the use of MySQLdb for
database connection and complex querying with JOIN statements, using
command-line arguments for database credentials. The script ensures operations
are performed in a safe context using a 'with' statement for resource management.
"""

import MySQLdb
from sys import argv

if __name__ == '__main__':
    """
    Connect to the MySQL database using credentials and database name
    provided as command-line arguments. Retrieves cities and their
    corresponding states in an orderly manner.
    """
    db = MySQLdb.connect(
        host="localhost",  # Database server address
        user=argv[1],      # Database username
        port=3306,         # Database server port
        passwd=argv[2],    # Database password
        db=argv[3]         # Database name
    )

    # Execute a query to join cities and states, ordering by cities' IDs
    with db.cursor() as cursor:
        cursor.execute("SELECT cities.id, cities.name, states.name \
                        FROM cities JOIN states ON cities.state_id = states.id \
                        ORDER BY cities.id ASC")

        # Fetch and print all rows that match the query
        rows = cursor.fetchall()

        if rows is not None:
            for row in rows:
                print(row)
