#!/usr/bin/python
import psycopg2
from config import config


def add_details(name, phone):

    conn = None
    try:
        # read database configuration
        params = config()
        # connect to the PostgreSQL database
        conn = psycopg2.connect(**params)
        # create a cursor object for execution
        cur = conn.cursor()

        # call a stored procedure
        cur.execute('CALL add_new_details(%s,%s)', (name, phone))

        # commit the transaction
        conn.commit()

        # close the cursor
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

if __name__ == '__main__':
    add_details('OLEG', '33434434')
