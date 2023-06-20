#!/usr/bin/python3
"""
A script that lists all cities from the database hbtn_0e_4_usa
"""


import MySQLdb
from sys import argv


if __name__ == "__main__":
    try:
        conn = MySQLdb.connect(user=argv[1],
                               passwd=argv[2], db=argv[3], port=3306)
        with conn.cursor() as cur:
            cur.execute(
                    """
                    SELECT cities.id, cities.name, states.name
                    FROM cities
                    JOIN states
                    ON states.id = cities.state_id
                    ORDER BY cities.id ASC
                    """)
            result = cur.fetchall()
            for cities in result:
                print(cities)
    except Exception as e:
        print(f"Error: {e}")
    finally:
        cur.close()
        conn.close()
