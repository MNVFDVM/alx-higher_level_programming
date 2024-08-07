#!/usr/bin/python3
"""
Lists all State objects from the database hbtn_0e_6_usa.
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: {} <username> <password> <database>".format(sys.argv[0]))
        sys.exit(1)

    username, password, database = sys.argv[1], sys.argv[2], sys.argv[3]

    try:
        # Establish connection to MySQL server running on localhost at port 3306
        engine = create_engine(f'mysql+mysqldb://{username}:{password}@localhost:3306/{database}',
                               pool_pre_ping=True)

        # Create a configured "Session" class
        Session = sessionmaker(bind=engine)

        # Create a Session instance
        with Session() as session:
            # Query all State objects and print in the specified format
            states = session.query(State).order_by(State.id).all()
            for state in states:
                print("{}: {}".format(state.id, state.name))

    except Exception as e:
        print("An error occurred:", e)
        sys.exit(1)
