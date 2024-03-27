#!/usr/bin/python3
"""Lists all states  starting with ‘N’ from the database hbtn_0e_0_usa"""
import MySQLdb
from sys import argv

if __name__ == "__main__":

    # connect to database
    db = MySQLdb.connect(
        host="localhost", port=3306,
        user=argv[1],
        passwd=argv[2],
        db=argv[3])

    # Cursor
    cur = db.cursor()

    # Exécute une requête SQL
    cur.execute(
        "SELECT * \
        FROM `states` \
        WHERE BINARY `name` = '{}'".format(argv[4])
    )

    [print(state) for state in cur.fetchall()]
