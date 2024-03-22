#!/usr/bin/python3
"""
script that prints that adds the State object
Louisiana to the database `hbtn_0e_6_usa`.
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
    Main execution block that connects to the database, adds a new State
    object for 'Louisiana', and prints the ID of the new state.
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
    # Creating a new State object for 'Louisiana'.
    new_state = State(name="Louisiana")
    # Adding the new state object to the session.
    session.add(new_state)
    # Committing the changes to the database.
    session.commit()
    # Printing the ID of the newly added state.
    print('{0}'.format(new_state.id))
    # Closing the session.
    session.close()
