#!/usr/bin/python3
'''
takes in the name of a state as an argument and lists * cities
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
    cursor.execute("""SELECT cities.name FROM
                cities INNER JOIN states ON states.id=cities.state_id
                WHERE states.name=%s""", (sys.argv[4],))

    cities = cursor.fetchall()

    idx = 0
    for city in cities:
        if idx != 0:
            print(", ", end="")
        print("%s" % city, end="")
        idx += 1
    print("")

    cursor.close()
    db.close()
