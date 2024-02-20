#!/usr/bin/python3
'''
Adds the State object 
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

    new_state_obj = State(name='Louisiana')
    db_session.add(new_state_obj)
    db_session.commit()
    print(new_state_obj.id)
    db_session.close()
