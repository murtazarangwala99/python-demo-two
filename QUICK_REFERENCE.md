# 🎯 QUICK REFERENCE - Using pyproject.toml for Dependencies

## ✅ THE WORKING STRUCTURE

```
flask-todo-proper/
│
├── pyproject.toml          ← Dependencies here!
├── config.toml             ← App settings
├── README.md
├── STEP_BY_STEP.md
│
└── src/                    ← MUST HAVE THIS!
    └── flask_todo_app/
        ├── __init__.py     ← REQUIRED!
        ├── app.py
        └── templates/
            └── index.html
```

## 📦 ONE COMMAND INSTALLATION

```bash
pip install -e .
```

This reads `pyproject.toml` and installs Flask + tomli automatically!

## 🚀 THREE WAYS TO RUN

```bash
# Method 1: Command line tool
flask-todo

# Method 2: Python module
python -m flask_todo_app.app

# Method 3: Direct
cd src
python flask_todo_app/app.py
```

## 🔑 KEY POINTS

1. **src-layout is REQUIRED** for `pip install -e .` to work
2. **pyproject.toml** must be in project root
3. **__init__.py** makes it a package (required!)
4. Run `pip install -e .` from project root (not from src/)

## 📝 WHAT'S IN pyproject.toml

```toml
[project]
dependencies = [
    "Flask>=3.0.0",    ← Installed automatically
    "tomli>=2.0.1",    ← Installed automatically
]
```

## ⚙️ WHAT'S IN config.toml

```toml
[app]
port = 5000        ← Change this to use different port
debug = true       ← Set false for production

[settings]
max_todo_length = 200  ← Customize as needed
```

## ✨ WHY THIS WORKS

- **src-layout** prevents "multiple top-level packages" error
- **Proper package structure** with `__init__.py`
- **Modern Python standard** (PEP 518/621)
- **No scripts needed** - pure pyproject.toml!

## 🎉 FINAL CHECKLIST

- [ ] Download all files
- [ ] Keep the exact folder structure (src/flask_todo_app/)
- [ ] Open terminal in project root
- [ ] Run: `pip install -e .`
- [ ] Run: `flask-todo`
- [ ] Open: http://localhost:5000

**That's it! Pure pyproject.toml dependency management! 🚀**
