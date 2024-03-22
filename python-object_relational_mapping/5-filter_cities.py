#!/usr/bin/python3
"""
Module for listing cities of a specified state from a database.

This script accepts the name of a state as an argument and lists all cities
of that state from the 'hbtn_0e_4_usa' database. It demonstrates secure
database interaction using MySQLdb, with command-line arguments for database
credentials and the state name. The script ensures safe query execution with
parameterized queries to prevent SQL injection.
"""

import MySQLdb
from sys import argv

if __name__ == '__main__':
    """
    Connects to the MySQL database using credentials and database name
    provided as command-line arguments. Retrieves cities belonging to
    a specified state.
    """
    db = MySQLdb.connect(
        host="localhost",  # Database server address
        user=argv[1],      # Database username
        port=3306,         # Database server port
        passwd=argv[2],    # Database password
        db=argv[3]         # Database name
    )

    # Execute a query to fetch cities of a given state in a secure manner
    with db.cursor() as cursor:
        cursor.execute("""
                    SELECT cities.name
                FROM cities JOIN states ON cities.state_id = states.id
                WHERE states.name LIKE BINARY %(state_name)s
                ORDER BY cities.id ASC""", {'state_name': argv[4]})

        # Fetch all rows returned by the query
        rows = cursor.fetchall()

    # Print the names of the cities for the specified state
    if rows:
        print(", ".join([row[0] for row in rows]))
