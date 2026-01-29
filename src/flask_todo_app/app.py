from flask import Flask, render_template, request, redirect, url_for, flash
import sqlite3
from pathlib import Path
import sys

# TOML loader (Python 3.11+ vs older)
if sys.version_info >= (3, 11):
    import tomllib
else:
    import tomli as tomllib


PROJECT_ROOT = Path(__file__).resolve().parents[2]
PYPROJECT_FILE = PROJECT_ROOT / "pyproject.toml"


def load_config():
    """Load application config from pyproject.toml."""
    if not PYPROJECT_FILE.exists():
        raise RuntimeError("pyproject.toml not found")

    with open(PYPROJECT_FILE, "rb") as f:
        data = tomllib.load(f)

    try:
        return data["tool"]["flask_todo_app"]
    except KeyError:
        raise RuntimeError("Missing [tool.flask_todo_app] config in pyproject.toml")


# Load configuration once
config = load_config()

# Flask app
app = Flask(__name__)
app.secret_key = "change-this-secret-key-in-production"

# Database config
DATABASE = PROJECT_ROOT / config["database"]["filename"]


def get_db_connection():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn


def init_db():
    conn = get_db_connection()
    conn.execute(
        """
        CREATE TABLE IF NOT EXISTS todos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            task TEXT NOT NULL,
            completed BOOLEAN NOT NULL DEFAULT 0,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
        """
    )
    conn.commit()
    conn.close()


@app.route("/")
def index():
    conn = get_db_connection()
    todos = conn.execute(
        "SELECT * FROM todos ORDER BY created_at DESC"
    ).fetchall()
    conn.close()
    return render_template("index.html", todos=todos, config=config)


@app.route("/add", methods=["POST"])
def add_todo():
    task = request.form.get("task", "").strip()
    max_length = config["settings"]["max_todo_length"]

    if not task:
        flash("Task cannot be empty!", "error")
    elif len(task) > max_length:
        flash(f"Task cannot exceed {max_length} characters!", "error")
    else:
        conn = get_db_connection()
        conn.execute("INSERT INTO todos (task) VALUES (?)", (task,))
        conn.commit()
        conn.close()
        flash("Task added successfully!", "success")

    return redirect(url_for("index"))


@app.route("/toggle/<int:todo_id>")
def toggle_todo(todo_id):
    conn = get_db_connection()
    conn.execute(
        "UPDATE todos SET completed = NOT completed WHERE id = ?", (todo_id,)
    )
    conn.commit()
    conn.close()
    return redirect(url_for("index"))


@app.route("/delete/<int:todo_id>")
def delete_todo(todo_id):
    conn = get_db_connection()
    conn.execute("DELETE FROM todos WHERE id = ?", (todo_id,))
    conn.commit()
    conn.close()
    flash("Task deleted successfully!", "success")
    return redirect(url_for("index"))


@app.route("/clear-completed")
def clear_completed():
    conn = get_db_connection()
    result = conn.execute("DELETE FROM todos WHERE completed = 1")
    count = result.rowcount
    conn.commit()
    conn.close()

    if count:
        flash(f"Cleared {count} completed task(s)!", "success")
    else:
        flash("No completed tasks to clear.", "info")

    return redirect(url_for("index"))


def main():
    init_db()
    app.run(
        debug=config["app"]["debug"],
        host=config["app"]["host"],
        port=config["app"]["port"],
    )


if __name__ == "__main__":
    main()
