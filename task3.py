import psycopg2
from config import config

new_users = [
    ['John', '1234567890'],
    ['Jane', '5555555555'],
    ['Bob Jones', '123-456'],
    ['Mary Brown', 'abc-def-ghij']
] 
params = config()

conn = psycopg2.connect(**params)

def insert_users(conn, new_users):
    cur = conn.cursor()
    cur.callproc('insert_users', (new_users,))
    result = cur.fetchall()
    if len(result) > 0:
        print("Incorrect data:")
        for row in result:
            print(row[0], row[1])
    else:
        print("All data inserted successfully.")
    conn.commit()

# Call the insert_users function
insert_users(conn, new_users)

# Close the database connection
conn.close()