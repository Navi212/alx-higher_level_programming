#!/usr/bin/python3
"""
Lists all states from the database hbtn_0e_0_usa
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
                ORDER BY states.id ASC
                """)
        result = cur.fetchall()
        for states in result:
            print(states)
    except Exception as e:
        print(f"Error: {e}")
    finally:
        cur.close()
        conn.close()
