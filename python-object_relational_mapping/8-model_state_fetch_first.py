#!/usr/bin/python3
"""
Module for printing the first State object from a database.

This script uses SQLAlchemy ORM for interacting with the `hbtn_0e_6_usa`
database to retrieve and print the first State object. It showcases database
connection setup, session creation, and ORM querying, utilizing command-line
arguments for database access credentials. The output format employs the
`.format()` method for string formatting.
"""

from sys import argv
from model_state import State, Base  # Importing the State model and Base
# Importing create_engine to create an engine
from sqlalchemy import create_engine
# Importing sessionmaker to create a session
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    """
    Connects to the database using SQLAlchemy ORM, retrieves, and prints
    the first State object using the .format() method for string formatting.
    """

    # Construct the database URL from command-line arguments
    database_url = "mysql+mysqldb://{}:{}@localhost:3306/{}".format(
        argv[1], argv[2], argv[3])

    # Create an engine that serves as the core interface to the database
    engine = create_engine(database_url)

    # Bind the sessionmaker to the engine, enabling session creation
    Session = sessionmaker(bind=engine)

    # Instantiate a session
    session = Session()

    # Query for the first State object in the database, ordered by its ID
    state = session.query(State).order_by(State.id).first()

    # Check if the State object exists and print its details using .format();
    # otherwise, print "Nothing"
    if state is not None:
        # Print the ID and name of the first State object
        print('{0}: {1}'.format(state.id, state.name))
    else:
        # If no State object was found, print "Nothing"
        print("Nothing")
