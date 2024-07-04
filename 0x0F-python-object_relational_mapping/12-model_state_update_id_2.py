#!/usr/bin/python3
"""Changes the name of the State object where id = 2 to "New Mexico" in the database hbtn_0e_6_usa."""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: {} username password database".format(sys.argv[0]))
        sys.exit(1)

    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    # Establish connection to MySQL server running on localhost at port 3306
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(username, password, database), pool_pre_ping=True)

    # Create a configured "Session" class
    Session = sessionmaker(bind=engine)

    # Create a Session instance
    session = Session()

    # Query for the State object with id = 2
    state_to_update = session.query(State).filter_by(id=2).first()

    # If state with id = 2 exists, update its name to "New Mexico"
    if state_to_update:
        state_to_update.name = "New Mexico"
        session.commit()
        print("Name updated successfully.")
    else:
        print("State with id = 2 not found.")

    # Close the session
    session.close()
