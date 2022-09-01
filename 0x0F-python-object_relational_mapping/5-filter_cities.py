#!/usr/bin/python3
"""
    Script that takes in arguments and displays all values in the
    states table of hbtn_0e_0_usa where name matches the argument.
    But this time, write one that is safe from MySQL injections!
"""


from sys import argv
import MySQLdb


def main():
    db = MySQLdb.connect('localhost', argv[1], argv[2], argv[3])
    cur = db.cursor()
    request = "SELECT cities.name, states.name FROM cities\
        LEFT JOIN states ON cities.state_id = states.id\
        WHERE states.name = '{}'".format(argv[4])
    cur.execute(request)
    rows = cur.fetchall()
    newList = []
    for row in rows:
        newList.append(row[0])
    print(*newList, sep=", ")


if __name__ == "__main__":
    main()
