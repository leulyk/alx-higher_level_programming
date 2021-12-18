#!/usr/bin/python3

"""
    Delete all states which have an 'a' in their name
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from sys import argv
from model_state import Base, State


if __name__ == "__main__":
    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}".format(
                            argv[1], argv[2], argv[3]))
    session = Session(bind=engine)

    states_to_delete = session.query(State)\
                              .filter(State.name.like("%a%"))\
                              .delete(synchronize_session='fetch')

    session.commit()
