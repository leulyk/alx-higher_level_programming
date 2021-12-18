#!/usr/bin/python3

"""
    list all State objects
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from model_state import Base, State
from sys import argv


if __name__ == "__main__":
    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}".format(
                            argv[1], argv[2], argv[3]))
    session = Session(bind=engine)
    states = session.query(State).filter(State.name.like("%a%"))

    for state in states:
        print("{}: {}".format(state.id, state.name))
