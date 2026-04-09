# Day 02 - Learn By Teaching: Data Types, Input, and SQL Basics

[![Day 02](https://img.shields.io/badge/Day-02-0f766e?style=for-the-badge)](https://github.com/)
[![HTML](https://img.shields.io/badge/HTML-5-e34f26?style=for-the-badge&logo=html5&logoColor=white)](https://developer.mozilla.org/en-US/docs/Web/HTML)
[![Python](https://img.shields.io/badge/Python-3.13%2B-3776ab?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![MySQL](https://img.shields.io/badge/MySQL-8.0-4479a1?style=for-the-badge&logo=mysql&logoColor=white)](https://dev.mysql.com/)
[![Status](https://img.shields.io/badge/Status-Active_Learning-f59e0b?style=for-the-badge)]()

> Day 2 is written like a mini classroom. It explains what to run, why it works, and what mistakes beginners should avoid.

---

## Lesson Goals

By the end of this lesson, students should be able to:

1. Identify Python data types using `type()`
2. Convert values between `str`, `int`, and `float`
3. Explain why `input()` causes type-related bugs
4. Create and query a SQL table using `CREATE`, `INSERT`, and `SELECT`
5. Use basic HTML text tags with meaning (`strong`, `em`, `sup`, `sub`)

## What Is In This Folder

| File | What Students Learn |
|------|----------------------|
| [index.html](index.html) | Headings, paragraphs, comments, emphasis tags, superscript and subscript |
| [practice.py](practice.py) | Data types, conversion, user input, and mini age calculator |
| [practice.sql](practice.sql) | SQL data types, table creation, inserts, selects, filtering, and NULL |
| [README.md](README.md) | Full Day 2 teaching guide |

## Suggested Class Flow (45-60 Minutes)

1. Run HTML file and observe text formatting
2. Run Python file and test type conversion behavior
3. Execute SQL file and inspect query results
4. Complete the practice tasks in this README
5. Explain one concept to a friend (peer teaching)

## Part 1: HTML Teaching Notes

The HTML file teaches structure and text meaning:

- `h1`, `h2`, `h3` create heading hierarchy
- `p` creates paragraphs
- `hr` separates sections
- `strong` marks important text
- `em` marks emphasized text
- `sup` and `sub` are used for scientific notation (`E = MC²`, `H₂O`)
- `<!-- comment -->` stores notes for developers only

Teaching question for students:

- Why use `strong` instead of only changing font weight with style?

## Part 2: Python Teaching Notes

### Step A - Data Types

In `practice.py`, students should identify these first:

- `age = 20` -> `int`
- `price = 99.99` -> `float`
- `name = "Dhayalan"` -> `str`
- `is_active = True` -> `bool`

Then confirm using:

```python
print(type(age))
print(type(price))
print(type(name))
print(type(is_active))
```

### Step B - Type Conversion

Core rule: Python does not auto-add strings and numbers.

Wrong:

```python
"5" + 5
```

Correct:

```python
int("5") + 5
```

### Step C - Input Handling

`input()` always returns a string.

So for numeric operations:

```python
age = int(input("Enter your age: "))
height = float(input("Enter your height in cm: "))
```

### Step D - Mini Problem

The birth-year problem teaches backend logic:

1. Take input
2. Convert to number
3. Process data
4. Print result

## Part 3: SQL Teaching Notes

The SQL file introduces table thinking.

### Concepts students should learn

- Columns define structure
- Rows store actual data
- Data types protect data quality
- `SELECT` reads data
- `WHERE` filters data

### Query Flow To Teach

1. Select database:

```sql
USE onepiece_db;
```

2. Create table:

```sql
CREATE TABLE characters (
    name VARCHAR(50),
    age INT,
    crew_name TEXT
);
```

3. Insert rows:

```sql
INSERT INTO characters (name, age, crew_name)
VALUES ('luffy', 19, 'Straw_hat');
```

4. Read rows:

```sql
SELECT * FROM characters;
```

5. Filter rows:

```sql
SELECT * FROM characters WHERE age > 20;
```

### Important NULL Concept

- `NULL` means missing value
- `''` means empty text value
- Use `IS NULL`, not `= NULL`

## Expected Output Check

Students should be able to show:

1. A browser page with formatted headings and paragraph text
2. Python output for type checks and input-based responses
3. SQL query output from `characters` table

## Common Beginner Mistakes

- Mixing string and number in Python operations
- Forgetting conversion after `input()`
- Running queries on wrong table name
- Using `= NULL` instead of `IS NULL`
- Incorrectly closed HTML tags

## Practice Tasks For Fellow Students

1. Python: Ask for weight in kg and print in grams
2. Python: Ask for two numbers and print sum, difference, product
3. SQL: Insert 3 more rows into `characters`
4. SQL: Show only `name` and `crew_name`
5. HTML: Add one sentence using `strong`, `em`, `sup`, and `sub`

## Peer Teaching Challenge

Explain these without running code:

1. Why does `"10" + "5"` return `"105"`?
2. Why does SQL need `IS NULL`?

If your friend understands, you have taught Day 2 well.

## Run Instructions

### HTML

Open `index.html` in your browser.

### Python

```bash
python practice.py
```

### SQL

Run `practice.sql` inside MySQL Workbench or MySQL CLI.

## File Correction Notes (For Better Teaching)

- In `practice.py`, final output line should use `your_name` for consistency.
- In `practice.sql`, some lines mention `students` while this day creates `characters`.

Suggested Python fix:

```python
print(f"Your name is {your_name} and your approximate age is {age}")
```

Suggested SQL fix style:

```sql
SELECT * FROM characters WHERE name = 'luffy';
```

## Day 2 Recap

One big idea connects HTML, Python, and SQL:

- Input has a type
- Type changes behavior
- Correct type gives correct result

## Learning Checklist

- [ ] I can explain `int`, `float`, `str`, `bool`
- [ ] I understand why `input()` returns string
- [ ] I can convert input safely before calculations
- [ ] I can create and query a SQL table
- [ ] I can explain the difference between `NULL` and empty text

## Next Day

Continue to [Day 03](../Day_03/README.md).
