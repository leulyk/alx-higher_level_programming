#!/usr/bin/python3

"""
    Update the state with id 2 to 'New Mexico'
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from sys import argv
from model_state import State, Base


if __name__ == "__main__":
    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}".format(
                            argv[1], argv[2], argv[3]))
    session = Session(bind=engine)

    session.query(State).filter(State.id == 2).update({'name': 'New Mexico'})
    session.commit()
