#!/usr/bin/python3
"""
A script that takes in arguments and displays all values
in the states table of hbtn_0e_0_usa where name matches the argument.
But this time, write one that is safe from MySQL injections!
"""


import MySQLdb
from sys import argv


if __name__ == "__main__":
    try:
        conn = MySQLdb.connect(user=argv[1],
                               passwd=argv[2], db=argv[3], port=3306)
        with conn.cursor() as cur:
            cur.execute("""
                SELECT *
                FROM states
                WHERE `name` LIKE '{}'
                ORDER BY states.id ASC
                """.format(argv[4]))
            result = cur.fetchall()
            for names in result:
                print(names)
    except Exception as e:
        print(f"Error: {e}")
    finally:
        cur.close()
        conn.close()
