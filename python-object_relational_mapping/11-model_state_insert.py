#!/usr/bin/python3
"""
Script that adds Louisiana object to db
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

    # Execute for first matching state
    new_state = State(name="Louisiana")
    session.add(new_state)
    session.commit()

    # Print new obj id
    print("{}".format(new_state.id))

    # Close session
    session.close()
