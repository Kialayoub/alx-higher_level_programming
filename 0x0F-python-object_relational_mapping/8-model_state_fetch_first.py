#!/usr/bin/python3
'''
prints the first State Objectt
'''
from sqlalchemy.orm import sessionmaker
from model_state import State
from sqlalchemy import create_engine
from sys import argv

if __name__ == '__main__':
    db_engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'.format(argv[1], argv[2], argv[3]))
    SessionMaker = sessionmaker(bind=db_engine)
    db_session = SessionMaker()

    first_state = db_session.query(State).order_by(State.id).first()
    if first_state:
        print('{}: {}'.format(first_state.id, first_state.name))
    else:
        print('Nothing ... ')
    db_session.close()
