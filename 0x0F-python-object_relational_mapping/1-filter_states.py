#!/usr/bin/python3
'''
lists * states with a name starting with the lettre N
'''

import MySQLdb
import sys

if __name__ == '__main__':
    db = MySQLdb.connect(user=sys.argv[1],passwd=sys.argv[2],db=sys.argv[3],port=3306)

    cursor = db.cursor()
    cursor.execute("""SELECT * FROM states WHERE name LIKE BINARY 'N%' ORDER BY states.id""")

    states = cursor.fetchall()
    for state in states:
        print(state)
    cursor.close()
    db.close()
