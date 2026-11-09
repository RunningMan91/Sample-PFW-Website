import sqlite3
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

def get_db_connection():
    # Establishes connection to the sqlite file created by the shell script
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row  # Enables column access by name dictionary
    return conn

@app.route('/')
def index():
    # Read operation: Fetch records using plain SQL
    conn = get_db_connection()
    tasks = conn.execute('SELECT * FROM tasks').fetchall()
    conn.close()
    return render_template('index.html', tasks=tasks)

@app.route('/create', methods=('POST',))
def create():
    # Write operation: Create record via POST form submission
    title = request.form['title']
    description = request.form['description']

    if title:
        conn = get_db_connection()
        conn.execute('INSERT INTO tasks (title, description) VALUES (?, ?)',
                     (title, description))
        conn.commit()
        conn.close()
        
    return redirect(url_for('index'))

if __name__ == '__main__':
    # Starts server locally on debug mode for instant auto-reload
    app.run(debug=True)
