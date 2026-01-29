"""Flask TODO Application - Main Module"""

from flask import Flask, render_template, request, redirect, url_for, flash
import sqlite3
from pathlib import Path
import sys

# Handle TOML imports based on Python version
if sys.version_info >= (3, 11):
    import tomllib
else:
    import tomli as tomllib


def load_config():
    """Load configuration from TOML file."""
    # Try to find config.toml in multiple locations
    possible_paths = [
        Path.cwd() / "config.toml",  # Current directory
        Path(__file__).parent / "config.toml",  # Same directory as app
        Path(__file__).parent.parent.parent / "config.toml",  # Project root
    ]
    
    for config_path in possible_paths:
        if config_path.exists():
            with open(config_path, "rb") as f:
                return tomllib.load(f)
    
    # Default configuration if no config file found
    print("Warning: config.toml not found, using defaults")
    return {
        "app": {
            "name": "Flask TODO Application",
            "debug": True,
            "host": "0.0.0.0",
            "port": 5000
        },
        "database": {
            "filename": "todos.db"
        },
        "settings": {
            "max_todo_length": 200,
            "items_per_page": 10
        }
    }


# Load configuration
config = load_config()

# Create Flask app
app = Flask(__name__)
app.secret_key = "change-this-secret-key-in-production"

# Database configuration
DATABASE = config["database"]["filename"]


def get_db_connection():
    """Create a database connection."""
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn


def init_db():
    """Initialize the database with required tables."""
    conn = get_db_connection()
    conn.execute('''
        CREATE TABLE IF NOT EXISTS todos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            task TEXT NOT NULL,
            completed BOOLEAN NOT NULL DEFAULT 0,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    conn.commit()
    conn.close()
    print("✓ Database initialized successfully")


@app.route('/')
def index():
    """Display all TODO items."""
    conn = get_db_connection()
    todos = conn.execute('SELECT * FROM todos ORDER BY created_at DESC').fetchall()
    conn.close()
    return render_template('index.html', todos=todos, config=config)


@app.route('/add', methods=['POST'])
def add_todo():
    """Add a new TODO item."""
    task = request.form.get('task', '').strip()
    max_length = config["settings"]["max_todo_length"]
    
    if not task:
        flash('Task cannot be empty!', 'error')
    elif len(task) > max_length:
        flash(f'Task cannot exceed {max_length} characters!', 'error')
    else:
        conn = get_db_connection()
        conn.execute('INSERT INTO todos (task) VALUES (?)', (task,))
        conn.commit()
        conn.close()
        flash('Task added successfully!', 'success')
    
    return redirect(url_for('index'))


@app.route('/toggle/<int:todo_id>')
def toggle_todo(todo_id):
    """Toggle the completion status of a TODO item."""
    conn = get_db_connection()
    conn.execute('UPDATE todos SET completed = NOT completed WHERE id = ?', (todo_id,))
    conn.commit()
    conn.close()
    return redirect(url_for('index'))


@app.route('/delete/<int:todo_id>')
def delete_todo(todo_id):
    """Delete a TODO item."""
    conn = get_db_connection()
    conn.execute('DELETE FROM todos WHERE id = ?', (todo_id,))
    conn.commit()
    conn.close()
    flash('Task deleted successfully!', 'success')
    return redirect(url_for('index'))


@app.route('/clear-completed')
def clear_completed():
    """Delete all completed TODO items."""
    conn = get_db_connection()
    result = conn.execute('DELETE FROM todos WHERE completed = 1')
    count = result.rowcount
    conn.commit()
    conn.close()
    if count > 0:
        flash(f'Cleared {count} completed task(s)!', 'success')
    else:
        flash('No completed tasks to clear.', 'info')
    return redirect(url_for('index'))


def main():
    """Main entry point for the application."""
    print("=" * 60)
    print("Starting Flask TODO Application")
    print("=" * 60)
    init_db()
    print(f"App Name: {config['app']['name']}")
    print(f"Debug Mode: {config['app']['debug']}")
    print(f"Running on: http://{config['app']['host']}:{config['app']['port']}")
    print("=" * 60)
    
    app.run(
        debug=config["app"]["debug"],
        host=config["app"]["host"],
        port=config["app"]["port"]
    )


if __name__ == '__main__':
    main()
