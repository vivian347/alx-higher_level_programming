#!/usr/bin/python3
""" script that is safe from sql injections """

if __name__ == "__main__":
    import MySQLdb
    import sys
    db = MySQLdb.connect(
            host='localhost',
            user=sys.argv[1],
            passwd=sys.argv[2],
            db=sys.argv[3],
            port=3306,
            charset='utf8'
    )
    cur = db.cursor()
    cmd = "SELECT * FROM states WHERE name = %s ORDER BY id"
    cur.execute(cmd, (sys.argv[4],))
    rows = cur.fetchall()
    for r in rows:
        print("({}, '{}')".format(r[0], r[1]))

    cur.close()
    db.close()
