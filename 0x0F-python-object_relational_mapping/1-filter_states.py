#!/usr/bin/python3

"""
    Lists all states whose name starts with an 'N' from the database
"""

from sys import argv
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(user=argv[1], passwd=argv[2], db=argv[3])
    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE BINARY name like 'N%' ORDER BY id")
    for row in cur.fetchall():
        print(row)
