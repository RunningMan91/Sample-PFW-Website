# Sample-PFW-Website
Create a sample website using flask, python, HTML, CSS, shell scripting and SQL that meets the requirements of the PFW unit.

# Google AI Summary
Combining Flask (Python), HTML, CSS, SQL, and Shell Scripting creates a highly practical, robust engineering stack. Python/Flask acts as your backend router, SQL handles your data persistence, HTML/CSS powers your user interface, and shell scripting automates your database initialization, dependencies, and local deployment.
Here is a minimal, end-to-end blueprint for a Task Manager Web App using your exact tech stack.

1. Project Directory Structure

Flask relies on a strict folder layout to automatically locate your HTML markup (templates/) and stylesheets (static/):
text

flask_project/

│

├── init_db.sh          # Shell script to build database

├── schema.sql          # SQL file defining your tables

├── app.py              # Main Python/Flask backend execution file

│

├── static/

│   └── style.css       # Front-end styling rules

└── templates/

    └── index.html      # Front-end layout skeleton

Use code with caution.

2. The Database Layer (SQL & Shell Scripting)

We will use SQLite because it is built into Python and requires zero system configuration.

schema.sql

Define your relational database schema:
sql
DROP TABLE IF EXISTS tasks;

CREATE TABLE tasks (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    description TEXT
);
Use code with caution.

init_db.sh

Write a native Bash shell script to automate environment configuration, setup, and database seeding:
bash
#!/bin/bash
# init_db.sh

echo "⚡ Initializing local development environment..."

# 1. Initialize built-in SQLite database using the SQL schema
sqlite3 database.db < schema.sql
echo "✔ Database tables provisioned using schema.sql."

# 2. Check for Python virtual environment; build it if missing
if [ ! -d "venv" ]; then
    python3 -m venv venv
    echo "✔ Created isolated Python virtual environment (venv)."
fi

# 3. Activate venv and install micro-framework dependencies
source venv/bin/activate
pip install --upgrade pip
pip install flask

echo "🚀 Setup complete. Run 'source venv/bin/activate && python3 app.py' to launch!"
Use code with caution.
Make sure to give it execution permissions in your terminal before running it: chmod +x init_db.sh

3. The Core Backend (app.py)

This file boots your server, queries the SQL database, and routes context variables straight to your HTML views.
python
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
Use code with caution.

4. The Frontend Presentation Layer (HTML & CSS)


templates/index.html

Flask utilizes Jinja templates, allowing you to embed looping logic and conditional variables right inside your basic HTML document structure.
html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Task Tracker</title>
    <!-- Dynamically links to your static asset directory -->
    <link rel="stylesheet" href="{{ url_for('static', filename='style.css') }}">
</head>
<body>
    <div class="container">
        <h1>Task Manager</h1>
        
        <!-- Interactive Form submission handling -->
        <form action="{{ url_for('create') }}" method="POST" class="task-form">
            <input type="text" name="title" placeholder="Task Title" required>
            <textarea name="description" placeholder="Task Description..."></textarea>
            <button type="submit">Add Task</button>
        </form>

        <hr>

        <!-- Python-driven loop iterating over SQL query results -->
        <div class="task-list">
            {% for task in tasks %}
                <div class="task-card">
                    <h3>{{ task['title'] }}</h3>
                    <p>{{ task['description'] }}</p>
                </div>
            {% else %}
                <p>No tasks added yet!</p>
            {% endfor %}
        </div>
    </div>
</body>
</html>
Use code with caution.

static/style.css

A clean, minimal look to polish your elements:
css
body {
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    background-color: #f4f7f6;
    color: #333;
    padding: 40px;
}
.container {
    max-width: 600px;
    margin: 0 auto;
    background: #fff;
    padding: 30px;
    border-radius: 8px;
    box-shadow: 0 4px 6px rgba(0,0,0,0.1);
}
.task-form input, .task-form textarea {
    width: 100%;
    margin-bottom: 12px;
    padding: 10px;
    border: 1px solid #ccc;
    border-radius: 4px;
    box-sizing: border-box;
}
button {
    background-color: #007bff;
    color: white;
    border: none;
    padding: 10px 15px;
    cursor: pointer;
    border-radius: 4px;
}
button:hover { background-color: #0056b3; }
.task-card {
    background: #f9f9f9;
    padding: 15px;
    border-left: 4px solid #007bff;
    margin-top: 15px;
    border-radius: 4px;
}
Use code with caution.

How to Run Everything

1. Run ./init_db.sh to initialize your database and setup packages.
2. Run source venv/bin/activate to enter your virtual environment.
3. Run python3 app.py to fire up the server.
4. Navigate to http://127.0.0 in your browser.
