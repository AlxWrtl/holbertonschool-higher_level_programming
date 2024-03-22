#!/usr/bin/python3
"""
A script that lists all cities from a specific database.

This script is designed to connect to a MySQL database and list all cities,
sorted by their IDs in ascending order. The cities are fetched from the
'hbtn_0e_4_usa' database, and their names are listed alongside their corresponding
state names. This script exemplifies the use of MySQLdb for establishing a
database connection and executing SQL queries. It uses command-line arguments
to receive database connection details (username, password, and database name).
"""

import MySQLdb
from sys import argv


def list_cities():
    """
    Connects to the MySQL database using provided command-line arguments and lists
    all cities along with their corresponding state names, sorted by city IDs.
    """
    # Ensure the script does not execute when imported
    if __name__ == '__main__':
        # Establish a database connection
        db = MySQLdb.connect(
            host="localhost",  # Database server address
            user=argv[1],      # Database username
            passwd=argv[2],    # Database password
            db=argv[3],        # Database name
            port=3306          # Database server port
        )

        # Create a cursor object to execute the query
        with db.cursor() as cursor:
            cursor.execute("""
                SELECT cities.id, cities.name, states.name
                FROM cities
                JOIN states ON cities.state_id = states.id
                ORDER BY cities.id ASC
            """)

            # Fetch all rows matching the query and print them
            rows = cursor.fetchall()
            for row in rows:
                print(row)


# Call the function to list cities
list_cities()
