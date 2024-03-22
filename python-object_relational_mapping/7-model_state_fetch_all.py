#!/usr/bin/python3
"""
Module for listing State objects from a database.

This script utilizes SQLAlchemy ORM to interact with the `hbtn_0e_6_usa`
database, listing all State objects. It demonstrates database connection
setup, session creation, and ORM querying, making use of command-line
arguments for database access credentials.
"""

from sys import argv
from model_state import State, Base  # Importing the State model and Base
from sqlalchemy import create_engine  # Importing create_engine
from sqlalchemy.orm import sessionmaker  # Importing sessionmaker

if __name__ == "__main__":
    """
    Connects to the database using SQLAlchemy ORM, retrieves, and prints
    all State objects.
    """

    # Construct the database URL from command-line arguments
    database_url = "mysql+mysqldb://{}:{}@localhost:3306/{}".format(
        argv[1], argv[2], argv[3])

    # Create an engine that represents the core interface to the database
    engine = create_engine(database_url)

    # Bind a sessionmaker to the engine to enable database session creation
    Session = sessionmaker(bind=engine)

    # Instantiate a session
    session = Session()

    # Query the database to retrieve and print all State objects
    for state in session.query(State).order_by(State.id).all():
        print('{0}: {1}'.format(state.id, state.name))
