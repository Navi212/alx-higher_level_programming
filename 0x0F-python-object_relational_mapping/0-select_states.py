#!/usr/bin/python3

if __name__ == "__main__":
    import MySQLdb
    from sys import argv
    conn = MySQLdb.connect(user=argv[1], passwd=argv[2],
                           db=argv[3], port=3306)
    cur = conn.cursor()
    cur.execute("SELECT *FROM states;")
    result = cur.fetchall()
    for states in result:
        print(states)
