#!/usr/bin/python3
"""
A script that takes in an argument and displays all values
in the states table of hbtn_0e_0_usa where name matches the argument.
"""


import MySQLdb
from sys import argv


if __name__ == "__main__":
    try:
        conn = MySQLdb.connect(user=argv[1],
                               passwd=argv[2], db=argv[3], port=3306)
        cur = conn.cursor()
        cur.execute(
            """
            SELECT *
            FROM states
            WHERE BINARY `name` = '{}'
            ORDER BY states.id ASC""".format(argv[4]))
        result = cur.fetchall()
        for names in result:
            print(names)
    except Exception as e:
        print(f"Error: {e}")
    finally:
        cur.close()
        conn.close()
