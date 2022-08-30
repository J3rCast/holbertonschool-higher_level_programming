#!/usr/bin/python3
"""script that lists all states from the database hbtn_0e_0_usa"""


from sys import argv
import MySQLdb


db =\
    MySQLdb.connect(host='localhost', user=argv[1], passwd=argv[2], db=argv[3])
cur = db.cursor()
cur.execute("SELECT * FROM states ORDER BY id")
rows = cur.fetchall()
for row in rows:
    print(row)
