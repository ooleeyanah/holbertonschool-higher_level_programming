#!/usr/bin/python3
"""
Script that updates name of obj where id == 2
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

    # Find object where id == 2
    update_state = session.query(State).filter_by(id=2).first()

    # Update object name
    if update_state:
        update_state.name = 'New Mexico'
        session.commit()

    # Close session
    session.close()
