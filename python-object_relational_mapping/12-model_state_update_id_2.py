#!/usr/bin/python3
"""
script that change the name of a state object
from the database `hbtn_0e_6_usa`.
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
    Main execution block that connects to the database, finds a State
    object with ID 2, changes its name to 'New Mexico', and commits
    the change to the database.
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
    # Querying the database to find the state object with ID 2.
    state = session.query(State).filter(State.id == 2).first()
    # Changing the name of the state to 'New Mexico'.
    state.name = "New Mexico"
    # Committing the changes to the database.
    session.commit()
    # Closing the session.
    session.close()
