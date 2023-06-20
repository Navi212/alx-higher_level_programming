#!/usr/bin/python3

if __name__ == "__main__":
    import MySQLdb
    from sys import argv

    try:
        conn = MySQLdb.connect(user=argv[1],
                               passwd=argv[2], db=argv[3], port=3306)
        with conn.cursor() as cur:
            cur.execute(""" \
                    SELECT * \
                    FROM states \
                    WHERE `name` LIKE '{}' \
                    ORDER BY states.id ASC \
                    """.format(argv[4]))
            result = cur.fetchall()
            for names in result:
                print(names)

    except Exception as e:
        print(f"Error: {e}")
