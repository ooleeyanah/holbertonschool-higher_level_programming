#!/usr/bin/python3
"""
Script that deletes objects with a
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

    # Find objects with letter a
    delete_state = session.query(State).filter(State.name.like('%a%')).all()

    # Update object name
    for state in delete_state:
        session.delete(state)

    session.commit()

    # Close session
    session.close()
