import psycopg2
from configparser import ConfigParser
import pandas as pd

def config(filename='db_driver/database.ini', section='postgresql'):
    # create a parser
    parser = ConfigParser()
    # read config file
    parser.read(filename)

    # get section, default to postgresql
    db = {}
    if parser.has_section(section):
        params = parser.items(section)
        for param in params:
            db[param[0]] = param[1]
    else:
        raise Exception('Section {0} not found in the {1} file'.format(section, filename))

    return db

def get_current_items():
    """ Connect to the PostgreSQL database server """
    conn = None
    try:
        # read connection parameters
        params = config()

        # connect to the PostgreSQL server
        print('Connecting to the PostgreSQL database...')
        conn = psycopg2.connect(**params)
		
        # create a cursor
        cur = conn.cursor()
        
    #get table
        cur.execute('SELECT * from todos')
        
        data = cur.fetchall()
        res = pd.DataFrame(columns=["Id", "Description", "Status"])
        
        for item in data:
            res.loc[len(res.index)] = item

    # close the communication with the PostgreSQL
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            print('Database connection closed.')
        
        return res

def change_item_status(id, status):
    
    sql = """ UPDATE todos
                SET Status = %s
                WHERE id = %s"""
                
    """ Connect to the PostgreSQL database server """
    conn = None
    try:
        # read connection parameters
        params = config()

        # connect to the PostgreSQL server
        print('Connecting to the PostgreSQL database...')
        conn = psycopg2.connect(**params)
		
        # create a cursor
        cur = conn.cursor()
        cur.execute(sql, (status, id))
        
        updated_rows = cur.rowcount
        
        print(f"Updated Rows = {updated_rows}")

        conn.commit()
    # close the communication with the PostgreSQL
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            print('Database connection closed.')
   
def insert_item(text):
    

    sql = """INSERT INTO todos(name)
             VALUES(%s) RETURNING id;"""
                
    """ Connect to the PostgreSQL database server """
    conn = None
    try:
        # read connection parameters
        params = config()

        # connect to the PostgreSQL server
        print('Connecting to the PostgreSQL database...')
        conn = psycopg2.connect(**params)
		
        # create a cursor
        cur = conn.cursor()
        cur.execute(sql, (text,))
        
        new_id = cur.fetchone()[0]
                
        print(f"New task = {new_id}")

        conn.commit()
    # close the communication with the PostgreSQL
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
        raise error
    finally:
        if conn is not None:
            conn.close()
            print('Database connection closed.')
       
def delete_item(id):
    sql = "DELETE FROM todos WHERE id = %s"
                
    """ Connect to the PostgreSQL database server """
    conn = None
    try:
        # read connection parameters
        params = config()

        # connect to the PostgreSQL server
        print('Connecting to the PostgreSQL database...')
        conn = psycopg2.connect(**params)
		
        # create a cursor
        cur = conn.cursor()
        cur.execute(sql, (str(id),))
        
        count = cur.rowcount
                
        print(f"Deleted Rows = {count}")

        conn.commit()
    # close the communication with the PostgreSQL
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
        raise error
    finally:
        if conn is not None:
            conn.close()
            print('Database connection closed.')
 
 
if __name__ == '__main__':
    res = delete_item(3)
    
    print(get_current_items())