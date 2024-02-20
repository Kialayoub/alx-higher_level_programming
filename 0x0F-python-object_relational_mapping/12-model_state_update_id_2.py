#!/usr/bin/python3
'''
Change the name of a State 
'''
from sys import argv
from sqlalchemy.orm import sessionmaker
from model_state import State
from sqlalchemy import create_engine

if __name__ == '__main__':
    db_engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'.format(argv[1], argv[2], argv[3]))
    SessionMaker = sessionmaker(bind=db_engine)
    db_session = SessionMaker()
    states_to_update = db_session.query(State).filter(State.id == 2)
    for state_obj in states_to_update:
        state_obj.name = 'New Mexico'
    db_session.commit()
    db_session.close()
