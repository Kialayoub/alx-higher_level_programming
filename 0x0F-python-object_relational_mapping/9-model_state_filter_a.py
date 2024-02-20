#!/usr/bin/python3
'''
lists all State objects that contain the letter A
'''
from sqlalchemy.orm import sessionmaker
from model_state import State
from sys import argv
from sqlalchemy import create_engine

if __name__ == '__main__':
    db_engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'.format(argv[1], argv[2], argv[3]))
    SessionMaker = sessionmaker(bind=db_engine)
    db_session = SessionMaker()

    states_with_a = db_session.query(State).filter(
        State.name.contains('a')).order_by(State.id).all()
    for state_obj in states_with_a:
        print('{}: {}'.format(state_obj.id, state_obj.name))
    db_session.close()
