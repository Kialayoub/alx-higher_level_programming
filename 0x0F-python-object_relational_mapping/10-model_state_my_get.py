#!/usr/bin/python3
'''
prints the State object with the name passed as argument
'''
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from model_state import State
from sys import argv

if __name__ == '__main__':
    db_engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'.format(argv[1], argv[2], argv[3]))
    SessionMaker = sessionmaker(bind=db_engine)
    db_session = SessionMaker()

    found_state = db_session.query(State).filter(State.name == argv[4]).first()
    print('Not found' if not found_state else found_state.id)
    db_session.close()
