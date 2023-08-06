#!/usr/bin/python3
import MySQLdb
import sys

if len(sys.argv) != 4:
    print("Usage: python script.py <username> <password> <db_name>")
    sys.exit(1)

username, password, db_name = sys.argv[1], sys.argv[2], sys.argv[3]

try:
    db = MySQLdb.connect(host='localhost', port=3306, user=username, passwd=password, db=db_name)

    cursor = db.cursor()

    query = "SELECT * FROM states ORDER BY id ASC"
    cursor.execute(query)

    states = cursor.fetchall()

    for state in states:
        print(state)

except MySQLdb.Error as e:
    print(f"Error: {e}")

finally:
    cursor.close()
    db.close()
