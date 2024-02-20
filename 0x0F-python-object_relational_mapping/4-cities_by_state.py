#!/usr/bin/python3
'''
ists all cities from the db
'''

import MySQLdb
import sys

if __name__ == '__main__':
    db = MySQLdb.connect(
        port=3306,
        host='localhost',
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3])

    cursor = db.cursor()
    cursorexecute("""SELECT cities.id, cities.name, states.name FROM cities INNER JOIN states ON states.id=cities.state_id""")
    states = cursor.fetchall()

    for state in states:
        print(state)
