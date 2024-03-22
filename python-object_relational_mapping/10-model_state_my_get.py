#!/usr/bin/python3
"""
script that prints the State objects passes as
argument from the database `hbtn_0e_6_usa`.
"""

from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from sys import argv
from model_state import State, Base
"""
Importing the State model and Base for ORM mapping.
"""
"""
Importing create_engine to initialize database connection.
"""
"""
Importing sessionmaker to create a session for transactions.
"""

if __name__ == "__main__":
    """
    Main execution block that connects to the database and retrieves states
    based on a specified name passed as an argument.
    """

    # Constructing the database URL from command-line arguments.
    database_url = "mysql+mysqldb://{}:{}@localhost:3306/{}".format(
        argv[1], argv[2], argv[3])

    # Creating an engine to connect to the specified database.
    engine = create_engine(database_url)

    # Creating a Session class bound to the created engine.
    Session = sessionmaker(bind=engine)

    # Instantiating a session to interact with the database.
    session = Session()
    # Extracting the state name passed as an argument.
    state_name = argv[4]
    # Querying the database to find the state object with the given name.
    state = session.query(State).filter(State.name == state_name).first()
    # Checking if the state object is found and printing its ID.
    if state is not None:
        print('{0}'.format(state.id))
    else:
        # Printing a message if the state is not found.
        print("Not found")
