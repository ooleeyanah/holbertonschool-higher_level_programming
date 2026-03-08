#!/usr/bin/python3
"""
Script that lists all State objects from the database
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    # Get command line args
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    # Create engine connecting to MySQL
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        username, password, database), echo=False)

    # Create session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query all States ordered by id asc
    states = session.query(State).order_by(State.id).all()

    # Display results
    for state in states:
        print("{}: {}".format(state.id, state.name))

    # Close session
    session.close()
