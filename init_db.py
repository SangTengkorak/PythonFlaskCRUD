import psycopg2 
from config import load_config

config = load_config()

def create_table():
    command = '''CREATE TABLE IF NOT EXISTS todos (
                            id SERIAL PRIMARY KEY, 
                            item TEXT NOT NULL, 
                            completed BOOLEAN DEFAULT FALSE);'''

    try:
        config = load_config()
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                # execute the CREATE TABLE statement
                    cur.execute(command)
    except (psycopg2.DatabaseError, Exception) as error:
        print(error)

if __name__ == '__main__':
    create_table()