#!/usr/bin/python3
"""
Lists all states with a name starting with N (upper N).
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
                WHERE BINARY `name` LIKE 'N%'
                ORDER BY states.id ASC
                """)
        result = cur.fetchall()
        for names in result:
            print(names)
    except Exception as e:
        print(f"Error: {e}")
    finally:
        cur.close()
        conn.close()
