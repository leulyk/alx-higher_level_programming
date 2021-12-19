#!/usr/bin/python3

"""
    Prints all City objects from the database hbtn_0e_14_usa.
    The script takes 3 arguments: mysql username, mysql password
    and database name.
    The script should connect to a MySQL server running on localhost
    at port 3306.
    Results must be sorted in ascending order by cities.id
    Results must be display as <state name>: (<city id>) <city name>
    The code should not be executed when imported
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from model_city import City
from model_state import Base, State
from sys import argv


if __name__ == "__main__":
    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}".format(
                            argv[1], argv[2], argv[3]))
    session = Session(bind=engine)

    rows = session.query(State.name, City.id, City.name)\
                  .select_from(City)\
                  .join((State, State.id == City.state_id))

    for row in rows:
        print("{}: ({}) {}".format(row[0], row[1], row[2]))
