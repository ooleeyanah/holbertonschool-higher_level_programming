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

    # Query for first state only
    first_state = session.query(State).order_by(State.id).first()

    # Display results
    if first_state is None:
        print("Nothing")
    else:
        print(f"{first_state.id}: {first_state.name}")

    # Close session
    session.close()
