#!/usr/bin/python3
'''
list * states via SQLAlchemy
'''
from sqlalchemy.orm import sessionmaker
from model_state import State
from sys import argv
from sqlalchemy import create_engine

if __name__ == '__main__':
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'.format(argv[1], argv[2], argv[3]))
    IneSession = sessionmaker(bind=engine)
    session = InSession()

    for state in session.query(State).order_by(State.id):
        print('{}: {}'.format(state.id, state.name))
    session.close()
