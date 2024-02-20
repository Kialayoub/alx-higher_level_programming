#!/usr/bin/python3
'''
creates the “California” State with the  “San Francisco” City
'''
from sys import argv
from sqlalchemy import create_engine
from relationship_state import Base, State
from relationship_city import City
from sqlalchemy.orm import sessionmaker

if __name__ == '__main__':
    db_engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'.format(argv[1], argv[2], argv[3]))
    Base.metadata.create_all(db_engine)
    SessionMaker = sessionmaker(bind=db_engine)
    db_session = SessionMaker()

    new_state_obj = State(name='California')
    new_city_obj = City(name='San Francisco',
