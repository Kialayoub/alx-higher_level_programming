#!/usr/bin/python3
'''
takes in an argument and displays all values in the states
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
    cursor.execute("SELECT * FROM states WHERE name LIKE %s", (match, ))

    states = cursor.fetchall()
    for state in states:
        print(state)

    cursor.close()
    db.close()
