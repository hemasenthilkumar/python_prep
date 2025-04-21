# 📦 Day 1: Package Tracker CLI

A command-line tool to manage package deliveries — add, update, delete, and list tracked packages. Designed to reinforce CLI building, modular Python, file I/O, and clean code architecture.

---

## 🧠 Goal

Build a command-line tool to track your delivery packages:
- ✅ Add a package
- ✅ Update delivery status
- ✅ List all packages
- ✅ Remove a package

---

## 💡 Learning Objectives

| Area | Focus |
|------|-------|
| 🔧 CLI | Learn `argparse` inside out (subcommands, flags, help text) |
| 📁 Structure | Write Python like a package, not just a script |
| 📚 Data Persistence | Read/write JSON like a tiny database |
| 🧱 OOP (optional) | Model a `Package` class |
| ⚙️ Robustness | Input validation and meaningful error handling |
| 📦 Packaging | (Optional) Make it pip-installable with `setup.py` or `pyproject.toml` |

---

## 📂 Suggested File Structure

package_tracker/
├── main.py           # CLI entry point
├── tracker/
│   ├── __init__.py
│   ├── core.py       # Logic: add, list, update, delete
│   ├── db.py         # JSON read/write
│   └── models.py     # Package class (optional)
├── data/
│   └── packages.json # Data store
└── README.md

## 🧪 Sample Usage

```bash
python main.py add --name "Phone" --id "12345" --status "shipped"
python main.py list
python main.py update --id "12345" --status "delivered"
python main.py delete --id "12345"
```

## Stretch Goals (Optional)

✅ Pretty printing with tabulate or rich

✅ Add vendor tracking (Amazon, FedEx, etc.)

✅ Add search functionality by name or ID

✅ Swap JSON with SQLite for persistence

✅ Unit tests for core functionality

✅ --export to CSV option

✅ How to Learn the Most From It

|Focus Area |	What to Practice|
|---|---|
|CLI Design	| Use argparse subcommands (add, list, etc.) |
|Modularity |	Avoid dumping logic in main.py — isolate logic in modules |
|JSON | I/O	Read/write/update JSON with exception handling |
|Versioning	| Commit early and often using Git |
|Writing Clean Code |	Follow naming conventions, PEP8, and use docstrings |
|Polishing	|Add --help, error messages, README with usage examples |
