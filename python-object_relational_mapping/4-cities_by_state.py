#!/usr/bin/python3
""" SQL injection to delete all records of a table…"""
import sys
import MySQLdb

if __name__ == '__main__':

    db = MySQLdb.connect(
        host="localhost", port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3])

    # Création d'un curseur
    cur = db.cursor()

    # Exécution requêtes SQL
    cur.execute(
        "SELECT * FROM states \
        WHERE name=%s \
        ORDER BY states.id ASC", (sys.argv[4],)
    )

    # Récupération des résultats
    states = cur.fetchall()

    # Affichage des résultats
    for state in states:
        print(state)

    cur.close()
    db.close()
