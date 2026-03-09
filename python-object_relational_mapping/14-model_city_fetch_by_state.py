#!/usr/bin/python3
"""
Script that lists all City objects from the database
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City

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

    # Query all Cities ordered by id asc
    results = session.query(State, City).join(City, State.id == City.state_id).order_by(City.id).all()

    # Display results
    for state, city in results:
        print("{}: ({}) {}".format(state.name, city.id, city.name))

    # Close session
    session.close()
