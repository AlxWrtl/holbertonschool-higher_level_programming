#!/usr/bin/python3
"""
script that lists all State objects that contain
the letter a from the database `hbtn_0e_6_usa`.
"""

from sys import argv
from model_state import State, Base
# Importing the State model and Base for ORM mapping.
from sqlalchemy import create_engine
# Importing create_engine to initialize database connection.
from sqlalchemy.orm import sessionmaker
# Importing sessionmaker to create a session for transactions.

if __name__ == "__main__":
    # Main execution block that connects to the database and retrieves states.

    # Constructing the database URL from command-line arguments.
    database_url = "mysql+mysqldb://{}:{}@localhost:3306/{}".format(
        argv[1], argv[2], argv[3])

    # Creating an engine to connect to the specified database.
    engine = create_engine(database_url)

    # Creating a Session class bound to the created engine.
    Session = sessionmaker(bind=engine)

    # Instantiating a session to interact with the database.
    session = Session()

    # Querying the database for State objects containing the letter 'a'.
    states = session.query(State).filter(State.name.contains('a'))

    # Iterating through the query result set and printing each state.
    for state in states:
        print('{0}: {1}'.format(state.id, state.name))
