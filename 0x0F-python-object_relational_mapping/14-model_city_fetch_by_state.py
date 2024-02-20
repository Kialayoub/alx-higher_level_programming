#!/usr/bin/python3
'''
Prints all Cities in the db
'''
from sys import argv
from sqlalchemy import create_engine
from model_state import State
from model_city import City
from sqlalchemy.orm import sessionmaker

if __name__ == '__main__':
    db_engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'.format(argv[1], argv[2], argv[3]))
    SessionMaker = sessionmaker(bind=db_engine)
    db_session = SessionMaker()
    records = db_session.query(State, City).join(City).order_by(City.id).all()
    for state_obj, city_obj in records:
        print('{}: ({}) {}'.format(state_obj.name, city_obj.id, city_obj.name))
    db_session.close()
