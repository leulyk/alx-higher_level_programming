#!/usr/bin/python3

"""
    A script that lists all State objects, and corresponding City objects:

    Takes 3 arguments: mysql username, mysql password and database name
    You must only use one query to the database
    You must use the cities relationship for all State objects
    Results must be sorted in ascending order by states.id and cities.id
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from relationship_state import Base, State
from relationship_city import City
from sys import argv


if __name__ == "__main__":
    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}".format(
                            argv[1], argv[2], argv[3]))
    session = Session(bind=engine)

    states = session.query(State).all()

    for state in states:
        print("{}: {}".format(state.id, state.name))
        for city in state.cities:
            print("\t{}: {}".format(city.id, city.name))
