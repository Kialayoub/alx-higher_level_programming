#!/usr/bin/python3
'''
Deletes all State objects if the name containing the letter A 
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
    states_with_a = db_session.query(State).filter(State.name.contains('a')).all()
    for state_obj in states_with_a:
        db_session.delete(state_obj)
    db_session.commit()
    db_session.close()
