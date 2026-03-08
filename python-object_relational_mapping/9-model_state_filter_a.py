#!/usr/bin/python3
"""
Script that prints first State from db
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

    # Query for states with letter a
    state_a = session.query(State).filter(State.name.like('%a'))

    # Display results
    if state_a is None:
        print("Nothing")
    else:
        print(f"{state_a.id}: {state_a.name}")

    # Close session
    session.close()
