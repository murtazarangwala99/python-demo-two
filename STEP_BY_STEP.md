# VISUAL STEP-BY-STEP GUIDE

## 🎯 Goal: Install Dependencies Using ONLY pyproject.toml

No scripts, no requirements.txt - just `pip install -e .`!

---

## 📂 STEP 1: Understand Your Directory Structure

Your project should look like this:

```
flask-todo-app/
│
├── pyproject.toml           ← Dependencies defined HERE!
├── config.toml              ← App settings (port, debug, etc.)
├── README.md
│
└── src/                     ← All code goes in src/
    └── flask_todo_app/      ← Your package name
        │
        ├── __init__.py      ← Makes it a Python package
        ├── app.py           ← Your Flask application
        │
        └── templates/       ← Flask templates folder
            └── index.html   ← Your HTML template
```

**Important:** The `src/` folder is REQUIRED for `pip install -e .` to work!

---

## 💻 STEP 2: Open Terminal in Project Root

```bash
# Navigate to your project folder
cd C:/Users/MurtuzaRangwala/Desktop/flask-todo-app

# Verify you're in the right place
ls
# You should see: pyproject.toml, config.toml, src/, README.md
```

**Windows (PowerShell/CMD):**
```powershell
cd C:\Users\MurtuzaRangwala\Desktop\flask-todo-app
dir
```

**Windows (Git Bash):**
```bash
cd /c/Users/MurtuzaRangwala/Desktop/flask-todo-app
ls
```

---

## 📦 STEP 3: Install Using pyproject.toml

Run this ONE command:

```bash
pip install -e .
```

**What happens:**
```
Installing build dependencies ... done
Getting requirements to build editable ... done
Installing backend dependencies ... done
Preparing editable metadata ... done
Building wheels for collected packages: flask-todo-app
  Building editable for flask-todo-app (pyproject.toml) ... done
Successfully installed Flask-3.0.0 flask-todo-app-1.0.0 tomli-2.0.1
```

**That's it!** Flask and tomli are now installed from `pyproject.toml`.

---

## ✅ STEP 4: Verify Installation

```bash
# Test that the package is installed
python -c "import flask_todo_app; print('✓ Package installed successfully!')"
```

**Expected output:**
```
✓ Package installed successfully!
```

---

## 🚀 STEP 5: Run Your Application

You now have 3 ways to run the app:

### Method 1: Command Line Tool (Easiest!)
```bash
flask-todo
```

### Method 2: Python Module
```bash
python -m flask_todo_app.app
```

### Method 3: Direct Execution
```bash
cd src
python flask_todo_app/app.py
```

**All three methods work the same way!**

---

## 🌐 STEP 6: Open in Browser

Once the app starts, you'll see:

```
============================================================
Starting Flask TODO Application
============================================================
✓ Database initialized successfully
App Name: Flask TODO Application
Debug Mode: True
Running on: http://0.0.0.0:5000
============================================================
 * Serving Flask app 'app'
 * Debug mode: on
 * Running on http://127.0.0.1:5000
```

Open your browser to: **http://localhost:5000**

---

## 🎨 VISUAL COMPARISON

### ❌ OLD WAY (Doesn't work with pip install -e .)

```
project/
├── app.py
├── templates/
│   └── index.html
├── config.toml
└── pyproject.toml
```

**Problem:** Flat layout causes "multiple top-level packages" error!

### ✅ NEW WAY (Works perfectly!)

```
project/
├── pyproject.toml
├── config.toml
└── src/
    └── flask_todo_app/
        ├── __init__.py
        ├── app.py
        └── templates/
            └── index.html
```

**Solution:** src-layout is the modern standard!

---

## 🔍 UNDERSTANDING pyproject.toml

Open `pyproject.toml` and look at this section:

```toml
[project]
name = "flask-todo-app"
version = "1.0.0"
dependencies = [
    "Flask>=3.0.0",           ← Flask will be installed
    "tomli>=2.0.1",           ← tomli will be installed
]
```

**When you run `pip install -e .`, it reads this file and installs these packages!**

---

## 📝 QUICK REFERENCE COMMANDS

```bash
# Install package and dependencies
pip install -e .

# Run the application
flask-todo

# Uninstall
pip uninstall flask-todo-app

# Reinstall after adding new dependencies
pip install -e .

# Check if package is installed
pip list | grep flask-todo-app
```

---

## 🎯 CHECKLIST - Did You Do Everything Right?

- [ ] Created `src/` folder
- [ ] Created `src/flask_todo_app/` folder
- [ ] Added `__init__.py` in `src/flask_todo_app/`
- [ ] Put `app.py` in `src/flask_todo_app/`
- [ ] Created `templates/` folder in `src/flask_todo_app/`
- [ ] Put `index.html` in `src/flask_todo_app/templates/`
- [ ] Put `pyproject.toml` in project root
- [ ] Put `config.toml` in project root
- [ ] Ran `pip install -e .` from project root
- [ ] Ran `flask-todo` to start the app
- [ ] Opened http://localhost:5000 in browser

---

## 🐛 Common Mistakes

### Mistake 1: Running from wrong directory
```bash
# ❌ Wrong - running from inside src/
cd src
pip install -e .  # This won't work!

# ✅ Right - running from project root
cd flask-todo-app
pip install -e .  # This works!
```

### Mistake 2: Forgetting __init__.py
```
src/
└── flask_todo_app/
    ├── app.py         ← Won't work without __init__.py!
    └── templates/
```

**Must have:**
```
src/
└── flask_todo_app/
    ├── __init__.py    ← REQUIRED!
    ├── app.py
    └── templates/
```

### Mistake 3: Wrong folder name
```toml
# In pyproject.toml
[project]
name = "flask-todo-app"  ← Uses dashes

# But folder is:
src/flask_todo_app/      ← Uses underscores! ✓ Correct!
```

**Package names use underscores, PyPI names use dashes.**

---

## 🎉 SUCCESS!

If you followed all steps, you now have:
- ✅ A proper Python package structure
- ✅ Dependencies managed via pyproject.toml
- ✅ Working `pip install -e .` command
- ✅ A running Flask TODO application!

**This is the modern, correct way to structure Python projects!**

---

## 📚 Want to Learn More?

- [Python Packaging Guide](https://packaging.python.org/)
- [PEP 518 - pyproject.toml](https://peps.python.org/pep-0518/)
- [PEP 621 - Project Metadata](https://peps.python.org/pep-0621/)
- [src-layout vs flat-layout](https://packaging.python.org/en/latest/discussions/src-layout-vs-flat-layout/)
