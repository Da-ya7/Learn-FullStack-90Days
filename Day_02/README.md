# Day 02 - HTML, Python, SQL (Learn + Teach)

[![Day 01](https://img.shields.io/badge/Day-01-0f766e?style=for-the-badge)](https://github.com/)
[![HTML](https://img.shields.io/badge/HTML-5-e34f26?style=for-the-badge&logo=html5&logoColor=white)](https://developer.mozilla.org/en-US/docs/Web/HTML)
[![Python](https://img.shields.io/badge/Python-3.13%2B-3776ab?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![MySQL](https://img.shields.io/badge/MySQL-8.0-4479a1?style=for-the-badge&logo=mysql&logoColor=white)](https://dev.mysql.com/)
[![Status](https://img.shields.io/badge/Status-Active_Learning-f59e0b?style=for-the-badge)]()

![Learning Banner](https://img.shields.io/badge/Full--Stack%20Journey-Day%2001-111827?style=flat-square&labelColor=111827)
This Day 2 folder is for beginners who want to understand three core ideas:

1. How HTML text tags format and structure content
2. How Python data types and input conversion work
3. How SQL tables, inserts, and select queries work

If you can explain this README to a friend, you have learned Day 2 well.

## Files In Day 2

- `index.html` -> HTML headings, paragraphs, text formatting tags, quote, image
- `practice.py` -> Python data types, type conversion, user input
- `practice.sql` -> SQL data types, table creation, inserts, select queries

## 1) HTML - Concept + Code Explanation

### Main concepts

- HTML gives structure to a web page
- Tags can add meaning (`strong`, `em`, `cite`) and not just style
- Inline styles can change color and alignment
- `sup` and `sub` help display scientific text like E=MC2 and H2O

### Your `index.html` explained

1. `<meta charset="UTF-8">`
   - Lets the browser show many characters correctly.

2. Heading section:
   - `<h1>`, `<h2>`, `<h3>` create title hierarchy.
   - You centered and colored them using inline style.

3. Paragraph with formatting:
   - `<strong>` makes text important.
   - `<em>` adds emphasis.
   - `<sup>` and `<sub>` display power and chemical notation.
   - `<mark>` highlights text.
   - `<del>` and `<ins>` show removed and inserted text.
   - `<cite>` is used for title/reference style text.

4. `<blockquote>`
   - Used for a long quoted/reference statement.

5. `<img src="..." alt="Luffy">`
   - Displays an image from URL.
   - `alt` text is important for accessibility.

### What students should learn from this HTML file

- Difference between content tags and style
- How nesting tags changes meaning of text
- Why clean closing tags matter in HTML

## 2) Python - Concept + Code Explanation

File: `practice.py`

### Main concepts

- Python has data types: `int`, `float`, `str`, `bool`
- `type()` checks the type of a value
- `input()` always returns a string
- Type conversion is required for numeric operations

### Code walkthrough

1. Data type examples:

```python
age = 20
price = 99.99
name = "Dhayalan"
is_active = True
```

- `age` is integer
- `price` is decimal number
- `name` is text
- `is_active` is boolean

2. Type checking:

```python
print(type(age))
print(type(price))
print(type(name))
print(type(is_active))
```

3. Type conversion examples:

```python
age_str = "20"
age_int = int(age_str)
```

- Converts string "20" to integer 20.

```python
score = 100
message = "Your score: " + str(score)
```

- Converts number to string before concatenation.

```python
y = 9.8
print(int(y))
```

- `int(9.8)` becomes `9` (decimal part removed, not rounded).

4. User input:

```python
name = input("Enter your name:")
age = int(input("enter your age:"))
height = float(input("Enter your height in cm:"))
```

- Name stays string.
- Age and height are converted for calculation use.

5. Practice problem logic:

- Take name and birth year.
- Calculate age using current year.
- Print the result.

### Important note for students

In the final print line, variable name should be consistent:

```python
print(f"Your name is {your_name} and your approximate age is {age}")
```

Reason: `your_name` is what you captured from input.

## 3) SQL - Concept + Code Explanation

File: `practice.sql`

### Main concepts

- SQL columns use data types (`INT`, `VARCHAR`, `TEXT`, etc.)
- `CREATE TABLE` defines structure
- `INSERT INTO` adds data rows
- `SELECT` reads data
- `WHERE` filters rows
- `NULL` means missing value

### Code walkthrough

1. Database selection:

```sql
USE onepiece_db;
```

2. Table creation:

```sql
CREATE TABLE characters(
    name varchar(50),
    age int,
    crew_name text
);
```

- `name` stores short text.
- `age` stores whole number.
- `crew_name` stores text.

3. Insert rows:

```sql
INSERT INTO characters (name,age,crew_name)
VALUES ('luffy',19,'Straw_hat');
```

- Adds one character record.

4. Reading data:

```sql
SELECT * from characters;
SELECT name,crew_name from characters;
SELECT * FROM characters WHERE age > 20;
```

- First query: all columns, all rows.
- Second query: only selected columns.
- Third query: rows where condition is true.

5. NULL check concept:

```sql
SELECT * FROM characters WHERE crew_name IS NULL;
```

- Use `IS NULL`, not `= NULL`.

### Important note for students

Some lines in your SQL script use table name `students`, but this Day 2 script creates `characters`.
For consistency, keep one table name while learning.

## Common Beginner Mistakes In Day 2

1. Python: mixing string and int without conversion
2. Python: forgetting that `input()` returns string
3. SQL: changing table name accidentally (`students` vs `characters`)
4. SQL: using `= NULL` instead of `IS NULL`
5. HTML: missing proper closing tags in complex nested lines

## Practice For Other Students

1. HTML: Add one paragraph using `strong`, `em`, `sup`, and `sub`
2. Python: Ask user for two numbers and print sum
3. Python: Ask birth year and print age
4. SQL: Insert 3 more rows into `characters`
5. SQL: Show only `name` for age above 20

## Quick Run Guide

### HTML

Open `index.html` in browser.

### Python

```bash
python practice.py
```

### SQL

Run `practice.sql` in MySQL Workbench or MySQL CLI.

## Day 2 Summary

Day 2 teaches one powerful idea:

- Data has type
- Type affects behavior
- Correct type gives correct output

Keep practicing daily. Small steps every day build strong full-stack skills.
