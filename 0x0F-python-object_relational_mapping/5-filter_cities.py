#!/usr/bin/python3
"""
A script that takes in the name of a state as an argument and
lists all cities of that state, using the database hbtn_0e_4_usa
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
                    SELECT cities.name
                    FROM cities
                    JOIN states
                    ON states.id = cities.state_id
                    WHERE states.name = '{}'
                    ORDER BY cities.id ASC""".format(argv[4]))
            result = cur.fetchall()
            li_cities = []
            for cities in result:
                li_cities.append(cities[0])
            print(", ".join(li_cities))
    except Exception as e:
        print(f"Error: {e}")
    finally:
        cur.close()
        conn.close()
