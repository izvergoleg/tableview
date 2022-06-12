import psycopg2
from configs import config

def connect():

    """ Connect to the PostgreSQL database server """
    conn = None
    try:
        # read connection parameters
        params = config.config()

        # connect to the PostgreSQL server
        print('Connecting to the PostgreSQL database...')
        conn = psycopg2.connect(**params)

        # create a cursor
        cur = conn.cursor()

        # execute a statement
        print('PostgreSQL database version:')
        cur.execute('SELECT version()')

        # display the PostgreSQL database server version
        db_version = cur.fetchone()
        print(db_version)

        # close the communication with the PostgreSQL
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            print('Database connection closed.')

def get_data():
    """ query data from the person table """
    conn = None
    try:
        params = config.config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        cur.execute("SELECT * "
                    "FROM customers "                                  
                    "LIMIT 1000")
        rows = cur.fetchall()
        # print("The number of parts: ", cur.rowcount)
        # for row in rows:
        #     print(row)

        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

    return rows

def delete_pers(person_id):

    conn = None
    rows_deleted = 0
    print(person_id)
    try:
        # read database configuration
        params = config.config()
        # connect to the PostgreSQL database
        conn = psycopg2.connect(**params)
        # create a new cursor
        cur = conn.cursor()
        # execute the UPDATE  statement
        cur.execute("DELETE FROM customers WHERE id = %s", (person_id,))
        # get the number of updated rows
        rows_deleted = cur.rowcount
        # Commit the changes to the database
        conn.commit()
        # Close communication with the PostgreSQL database
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

    return rows_deleted

def update_row(person_id, *args):
    """ update surnamename based on the person id """
    sql = """ UPDATE customers SET "1" = %s, "3" = %s, "2" = %s,
     "4" = %s, "6" = %s, "5" = %s, "7" = %s, "8" = %s, "9" = %s, "10" = %s, "11" = %s  WHERE id = %s"""
    conn = None
    updated_rows = 0
    try:
        # read database configuration
        params = config.config()
        # connect to the PostgreSQL database
        conn = psycopg2.connect(**params)
        # create a new cursor
        cur = conn.cursor()
        # execute the UPDATE  statement
        cur.execute(sql, (*args, person_id))
        # get the number of updated rows
        updated_rows = cur.rowcount
        # Commit the changes to the database
        conn.commit()
        # Close communication with the PostgreSQL database
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

    return updated_rows

def getRowData(pers_id):
    """ query row from the customer table """
    _sql = """ SELECT * FROM customers WHERE id = %s """
    conn = None
    row = None
    pers = int(pers_id)
    try:
        params = config.config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        cur.execute(_sql, (pers,))
        row = cur.fetchone()
        # print("The number of parts: ", cur.rowcount)
        # for row in rows:
        #     print(row)
        # print(row)
        # cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

    return row