
# Day 01 - First Steps With HTML, Python, and SQL

[![Day 01](https://img.shields.io/badge/Day-01-0f766e?style=for-the-badge)](https://github.com/)
[![HTML](https://img.shields.io/badge/HTML-5-e34f26?style=for-the-badge&logo=html5&logoColor=white)](https://developer.mozilla.org/en-US/docs/Web/HTML)
[![Python](https://img.shields.io/badge/Python-3.13%2B-3776ab?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![MySQL](https://img.shields.io/badge/MySQL-8.0-4479a1?style=for-the-badge&logo=mysql&logoColor=white)](https://dev.mysql.com/)
[![Status](https://img.shields.io/badge/Status-Active_Learning-f59e0b?style=for-the-badge)]()

> Day 1 of the 90-day journey. This folder captures the first working examples of HTML, Python, and SQL, written as a clean reference for future practice and revision.

![Learning Banner](https://img.shields.io/badge/Full--Stack%20Journey-Day%2001-111827?style=flat-square&labelColor=111827)

---

## Overview


This day is focused on the fundamentals:


- Writing a basic HTML page with headings and metadata
- Practicing Python variables, printing, arithmetic, and simple calculations
- Creating and selecting a MySQL database

The goal is not just to run code, but to understand the role each layer plays in a full-stack workflow.

## What’s In This Folder


| File | Purpose |
|------|---------|
| [index.html](index.html) | First HTML page with headings for frontend learning |
| [practice.py](practice.py) | Python practice covering variables, arithmetic, and small exercises |
| [practice.sql](practice.sql) | SQL practice for database creation and connection checks |
| [README.md](README.md) | Day 1 notes, explanations, and learning summary |

## Visual Snapshot

```html
<!DOCTYPE html>
<html>
  <head>
    <meta charset="UTF-8">
    <title>My first day on html</title>
  </head>
  <body>
    <h1>im learing html,css,jjs,react for frontend</h1>
    <h2>and python for backend</h2>
    <h3>Mysql for database</h3>
  </body>
</html>
```

```python
print("Hello Fellow Learners")
print("this is day 1 in learning python")

name = "Daya"
age = "20"
height = 5.9
is_student = True
```

```sql
create database onepiece_db;
use onepiece_db;
SELECT DATABASE();
```

## HTML Notes

The HTML file is a simple starter page that introduces the main document structure:

- `<!DOCTYPE html>` declares HTML5
- `<meta charset="UTF-8">` allows emojis and non-ASCII characters
- `<title>` sets the browser tab text
- `<h1>`, `<h2>`, and `<h3>` give the page a simple content hierarchy

## Python Notes

The Python practice file covers the first concepts every beginner should be comfortable with:

- `print()` for output
- variables for storing text, numbers, and booleans
- arithmetic operators such as `+`, `-`, `*`, `/`, `%`, and `**`
- small problem-solving examples like a mini calculator and rectangle area calculation

Key takeaways from the file:

- `age` is currently stored as a string, which is fine for practice but would usually be an integer in real code
- the arithmetic examples help build comfort with operator behavior
- the mini calculator demonstrates how simple values can be combined into a result

## SQL Notes

The SQL practice file is intentionally minimal and confirms the basic workflow:

- create a database named `onepiece_db`
- switch to that database with `USE onepiece_db`
- verify the active database using `SELECT DATABASE()`

This is the foundation for later lessons involving tables, inserts, joins, and queries.

## Practical Outcome

By the end of Day 1, the setup should support three things:

1. A browser can open the HTML file
2. Python can run the practice script successfully
3. MySQL can create and select a database without errors

## Learning Checklist

- [ ] HTML file opens in the browser
- [ ] Python script runs without syntax errors
- [ ] Variables, print statements, and arithmetic are understood
- [ ] MySQL database creation works locally
- [ ] The active database can be confirmed with `SELECT DATABASE();`

## Next Day

Continue to [Day 02](../Day_02/README.md) for the next step in the learning path.
