#!/usr/bin/python3
'''
Lists all State objects, and corresponding Cities
'''
from sys import argv
from relationship_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_city import City

if __name__ == '__main__':
    db_engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'.format(argv[1], argv[2], argv[3]))
    Base.metadata.create_all(db_engine)
    SessionMaker = sessionmaker(bind=db_engine)
    db_session = SessionMaker()
    states_list = db_session.query(State).order_by(State.id).all()
    for state_obj in states_list:
        print('{}: {}'.format(state_obj.id, state_obj.name))
        for city_obj in state_obj.cities:
            print('\t{}: {}'.format(city_obj.id, city_obj.name))
    db_session.close()
