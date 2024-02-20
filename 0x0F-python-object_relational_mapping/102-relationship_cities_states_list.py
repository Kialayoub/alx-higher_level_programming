#!/usr/bin/python3
"""
Lists all Cities from the database 
"""
import sys
from relationship_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_city import City

if __name__ == '__main__':
    db_engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.
                           format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    SessionMaker = sessionmaker(bind=db_engine)
    db_session = SessionMaker()
    states = db_session.query(State).join(City).order_by(City.id).all()
    for state_obj in states:
        for city_obj in state_obj.cities:
            print("{}: {} -> {}".format(city_obj.id, city_obj.name, state_obj.name))
    db_session.close()
