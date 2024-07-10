import psycopg2 
from config import load_config

app = Flask(__name__)
config = load_config()
  
# Connect to the database 
conn =  psycopg2.connect(**config)
cur = conn.cursor()

# if you already have any table or not id doesnt matter this  
# will create a products table for you. 
cur.execute( 
    '''CREATE TABLE IF NOT EXISTS todos (
    id SERIAL PRIMARY KEY, 
    item TEXT NOT NULL, 
    completed BOOLEAN DEFAULT FALSE);''')

# Commit the changes
conn.commit()

# Close the cursor and connection
cur.close()
conn.close()
