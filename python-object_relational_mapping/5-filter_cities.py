#!/usr/bin/python3
"""
Lists all cities from db hbtn_0e_0_usa that matches input state SAFELY
"""
import MySQLdb
import sys


if __name__ == "__main__":
    # Get command line arguments
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]
    state_name_searched = sys.argv[4]

    # Connect to MySQL database
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=mysql_username,
        passwd=mysql_password,
        db=database_name
    )

    # Create cursor object
    cursor = db.cursor()

    # Execute query to select all states ordered by id
    cursor.execute("SELECT cities.name FROM cities LEFT JOIN states "
                    "ON cities.state_id = states.id WHERE states.name = %s "
                   "ORDER BY cities.id ASC", (state_name_searched,))

    # Fetch all results
    results = cursor.fetchall()

    # Display results
    city_names = [row[0] for row in results]
    print(", ".join(city_names))

    # Close cursor and database connection
    cursor.close()
    db.close()
