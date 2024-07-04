#!/usr/bin/python3
"""Lists all State objects from the database hbtn_0e_6_usa that contain the letter 'a'."""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    # Establish connection to MySQL server running on localhost at port 3306
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)

    # Create a configured "Session" class
    Session = sessionmaker(bind=engine)

    # Create a Session instance
    session = Session()

    # Query State objects that contain the letter 'a', sorted by id in ascending order
    states_with_a = session.query(State).filter(State.name.like('%a%')).order_by(State.id).all()

    # Print the results in the specified format
    for state in states_with_a:
        print("{}: {}".format(state.id, state.name))

    # Close the session
    session.close()
