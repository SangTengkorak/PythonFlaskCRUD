from flask import Flask, render_template, request, redirect, url_for 
import psycopg2 
from config import load_config

app = Flask(__name__)
config = load_config()
  
@app.route('/')
def index():
    # Connectiong to the PostgreSQL server
    conn =  psycopg2.connect(**config)
    cur = conn.cursor()
    
    # Select all products from the table 
    cur.execute('''SELECT * FROM todos''') 
  
    # Fetch the data 
    data = cur.fetchall() 
  
    # close the cursor and connection 
    cur.close() 
    conn.close() 
  
    return render_template('index.html', data=data) 

@app.route('/create', methods=['POST'])
def create(): 
    conn =  psycopg2.connect(**config)
    cur = conn.cursor()
  
    # Get the data from the form 
    item = request.form['item'] 
    completed = request.form['completed'] 
  
    # Insert the data into the table 
    cur.execute( 
        '''INSERT INTO todos (item, completed) VALUES (%s, %s)''', 
        (item, completed)) 
  
    # commit the changes 
    conn.commit() 
  
    # close the cursor and connection 
    cur.close() 
    conn.close() 
  
    return redirect(url_for('index')) 

@app.route('/update', methods=['POST']) 
def update(): 
    conn =  psycopg2.connect(**config)
    cur = conn.cursor()
  
    # Get the data from the form 
    item = request.form['item'] 
    completed = request.form['completed'] 
    id = request.form['id'] 
  
    # Update the data in the table 
    cur.execute( 
        '''UPDATE todos SET item=%s, completed=%s WHERE id=%s''', (item, completed, id)) 
  
    # commit the changes 
    conn.commit() 
    return redirect(url_for('index'))

@app.route('/delete', methods=['POST']) 
def delete(): 
    conn =  psycopg2.connect(**config)
    cur = conn.cursor()
  
    # Get the data from the form 
    id = request.form['id'] 
  
    # Delete the data from the table 
    cur.execute('''DELETE FROM todos WHERE id=%s''', (id,)) 
  
    # commit the changes 
    conn.commit() 
  
    # close the cursor and connection 
    cur.close() 
    conn.close() 
  
    return redirect(url_for('index')) 

if __name__ == '__main__':
    app.run(debug=True) 