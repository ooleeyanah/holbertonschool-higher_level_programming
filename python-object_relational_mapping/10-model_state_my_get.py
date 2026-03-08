#!/usr/bin/python3
"""
Script that prints user input state
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
    state_name = sys.argv[4]

    # Create engine connecting to MySQL
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        username, password, database), echo=False)

    # Create session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Execute for first matching state
    user_input_state = session.query(State).filter_by(name=state_name).first()

    # Check if any results
    if user_input_state is None:
        print("Not found")
    else:
        print("{}".format(user_input_state.id))

    # Close session
    session.close()
