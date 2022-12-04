#!/usr/bin/python3

""" takes in arg and displays all values where name matches the arg """

if __name__ == "__main__":
    import MySQLdb
    import sys

    db = MySQLdb.connect(
            host="localhost",
            user=sys.argv[1],
            passwd=sys.argv[2],
            db=sys.argv[3],
            port=3306,
            charset='utf8'
    )

    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE name LIKE '%{}%' ORDER BY id".format(sys.argv[4]))
    rows= cur.fetchall()
    for r in rows:
        print("({},'{}')".format(r[0], r[1]))

    cur.close()
    db.close()
