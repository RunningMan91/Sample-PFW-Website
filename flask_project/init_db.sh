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
