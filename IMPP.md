# Starting Point (Your Current State)

You are here:

```
Pyyy2/2
├── config.toml
├── pyproject.toml
├── README.md
├── STEP_BY_STEP.md
├── QUICK_REFERENCE.md
├── src/
│   └── flask_todo_app/
│       ├── __init__.py
│       ├── app.py
│       └── templates/
│           └── index.html
```

No virtualenv assumed yet.

---

# STEP 0️⃣ (Optional but Recommended): Create Virtual Environment

### Command

```bash
python -m venv .venv
```

### What gets created

```
.venv/
 ├── Scripts/ (Windows)
 ├── Lib/
 └── pyvenv.cfg
```

### Why

* Isolates dependencies
* Prevents polluting global Python
* Required in real projects, CI/CD, Azure

### Commit?

❌ **NO** (`.venv/` goes in `.gitignore`)

---

### Activate it

```bash
source .venv/Scripts/activate   # Git Bash on Windows
```

(No files created, just shell state)

---

# STEP 1️⃣: Install the Project (THIS IS CRITICAL)

### Command

```bash
pip install -e .
```

This is the **most misunderstood command** in Python.

---

## What happens internally

### 1. `pyproject.toml` is read

* Finds:

  * project name
  * dependencies (Flask, tomli)
  * src layout

### 2. Dependencies are installed

Created in:

```
.venv/Lib/site-packages/
```

Example:

```
site-packages/
 ├── flask/
 ├── werkzeug/
 ├── tomli/
```

### 3. Your project is registered as a package

Created:

```
src/flask_todo_app.egg-info/
```

Contents:

* metadata
* version
* dependency info

### Why `.egg-info` exists

* Allows Python to do:

  ```python
  import flask_todo_app
  ```
* Enables editable mode (`-e`)

### Commit?

❌ **NO** (build artifact)

---

# STEP 2️⃣: Run the Application

You now have **3 valid ways**. I’ll explain **ONE correct way**.

---

## ✅ Correct Way (Recommended)

### Command

```bash
python -m flask_todo_app.app
```

---

## What happens internally

### 1. Python resolves the module

* Uses `.egg-info`
* Knows where `flask_todo_app` lives

### 2. `app.py` is executed

* `create_app()` runs
* Flask app instance created

---

## Files created AFTER FIRST RUN

### 🔹 `__pycache__/`

```
src/flask_todo_app/__pycache__/
 ├── app.cpython-312.pyc
 └── __init__.cpython-312.pyc
```

**Why**

* Python bytecode cache
* Faster imports next time

**Commit?**
❌ NO

---

### 🔹 `todos.db`

```
todos.db
```

**Who created it**

* Your Flask app (`init_db()`)

**Why**

* SQLite database
* Stores TODO tasks

**When**

* First HTTP request
* First page load (`/`)

**Commit?**
❌ NO

---

# STEP 3️⃣: Open Browser

```
http://localhost:5000
```

### What happens now

Each action creates DB changes:

| Action      | Effect                   |
| ----------- | ------------------------ |
| Add task    | INSERT row in `todos.db` |
| Delete task | DELETE row               |
| Refresh     | SELECT query             |

No new files are created after this point.

---

# STEP 4️⃣: Stop the App

```bash
CTRL + C
```

No files created or deleted.

---

# 🔍 Summary Table (COMMAND → FILE IMPACT)

| Command                | Files Created  | Purpose          | Commit? |
| ---------------------- | -------------- | ---------------- | ------- |
| `python -m venv .venv` | `.venv/`       | Isolated Python  | ❌       |
| `pip install -e .`     | `*.egg-info/`  | Package metadata | ❌       |
| Run app                | `__pycache__/` | Bytecode cache   | ❌       |
| First request          | `todos.db`     | App data         | ❌       |

---

# 🔥 Common Mistakes (I’ll Call Them Out)

❌ Running `python app.py` from random folders
❌ Not installing the package first
❌ Committing `.db` and `__pycache__`
❌ Thinking `.egg-info` is “important source code”

---

# 🧠 Mental Model (Remember This)

> **Source code = what YOU write**
> **Generated files = what TOOLS create**

Only source code belongs in Git.


