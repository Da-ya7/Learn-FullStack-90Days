# Day 01 — Your First Full-Stack Setup

[![Day](https://img.shields.io/badge/Day-01-0f766e?style=for-the-badge)](#)
[![HTML5](https://img.shields.io/badge/HTML-5-e34f26?style=for-the-badge&logo=html5&logoColor=white)](#)
[![Python](https://img.shields.io/badge/Python-3.11+-3776ab?style=for-the-badge&logo=python&logoColor=white)](#)
[![MySQL](https://img.shields.io/badge/MySQL-8.0+-4479a1?style=for-the-badge&logo=mysql&logoColor=white)](#)
[![Status](https://img.shields.io/badge/Status-Complete-10b981?style=for-the-badge)](#)
[![Last Updated](https://img.shields.io/badge/Last%20Updated-2026--04--10-gray?style=for-the-badge)](#)
[![Learning Focus](https://img.shields.io/badge/Focus-Foundations-orange?style=for-the-badge)](#)

> **Day 1 of 90:** Setting up your full-stack environment and understanding how HTML (frontend), Python (backend), and MySQL (database) work together.

---

## Table of Contents

- [Day Overview](#day-overview)
- [What You Built](#what-you-built)
- [What You Learned](#what-you-learned)
- [Why This Day Matters](#why-this-day-matters)
- [Core Concepts Explained](#core-concepts-explained)
- [File Inventory](#file-inventory)
- [Code Explanations](#code-explanations)
- [How to Run & Test](#how-to-run--test)
- [Key Takeaways](#key-takeaways)
- [Practice Tasks](#practice-tasks)
- [FAQ](#faq)
- [Summary](#summary)

---

## Day Overview

### What You Built

Three simple programs working on three different layers:
- **Frontend (HTML)**: A basic webpage with a title and three headings showing what you'll learn
- **Backend (Python)**: A script demonstrating variables, printing output, and arithmetic calculations
- **Database (MySQL)**: Created your first database and verified the connection

### What You Learned

1. **HTML fundamentals**: Document structure, meta tags, heading hierarchy
2. **Python fundamentals**: Variables, data types, printing, arithmetic operators
3. **SQL fundamentals**: Database creation, selection, basic commands

### Why This Day Matters

Day 1 is your **foundation**. You're touching all three core layers of a full-stack application:
- Frontend tells users what to do
- Backend processes the logic
- Database stores the information

By the end of this day, you understand the **three-layer architecture** that powers all modern web applications.

---

## Core Concepts Explained

### 1. **Variables (Python & General Programming)**

**Simple Explanation:**
A variable is a **named container** that holds information. Think of it like a labeled box where you store stuff.

**Real-World Analogy:**
Imagine a post office with numbered boxes. Box #1 is labeled "name" and holds a letter with "Daya" written on it. Box #2 is labeled "age" and holds a number card "20". When you need the information, you just say "give me what's in the 'name' box."

**Common Beginner Mistakes:**
- ❌ Using a variable name that conflicts with Python keywords (`class`, `for`, `if`, etc.)
- ❌ Forgetting that `age = "20"` makes age a text (string), not a number
- ❌ Using spaces or special characters in variable names (`my age` ❌ vs. `my_age` ✓)

**Quick Memory Tip:**
Variables = **named storage**. You define it once, use it many times. If you need to change the value later, you only change it in one place.

**Rule Example:**
```python
name = "Daya"        # Create a variable called "name" with value "Daya"
print(name)          # Use the variable—prints: Daya
name = "Alex"        # Change it—it's now "Alex"
print(name)          # prints: Alex
```

---

### 2. **Data Types (Python)**

**Simple Explanation:**
In Python, data comes in different **types**. The main types are:
- `str` (text/string): `"hello"`, `"20"`
- `int` (whole number): `42`, `-5`, `0`
- `float` (decimal number): `3.14`, `-2.5`, `5.0`
- `bool` (true/false): `True`, `False`

**Real-World Analogy:**
Think of filing cabinets with different sections:
- **String drawer**: holds written words/text
- **Integer drawer**: holds whole numbers only (no decimals)
- **Float drawer**: holds numbers with decimals
- **Boolean drawer**: holds yes/no or true/false answers

**Common Beginner Mistakes:**
- ❌ Thinking `age = "20"` and `age = 20` are the same (one is text, one is a number)
- ❌ Mixing types incorrectly: `result = "5" + 5` ❌ (can't add text and number directly)
- ❌ Not remembering Boolean values are `True` and `False`, not `"True"` or `true`

**Quick Memory Tip:**
**Strings** need quotes. **Numbers** don't. **Booleans** are always capitalized.

**Rule Example:**
```python
name = "Daya"        # str (text—notice the quotes)
age = 20             # int (number—no quotes)
height = 5.9         # float (decimal—no quotes)
is_student = True    # bool (true/false—no quotes, capitalized)
```

---

### 3. **Arithmetic Operators (Python)**

**Simple Explanation:**
Math operations in code. Use `+`, `-`, `*`, `/`, `%`, `**` to do calculations.

**Real-World Analogy:**
Like a calculator:
- `+` is addition: Earn $10 + earn $5 = $15 total
- `-` is subtraction: Have $20 - spend $8 = $12 left
- `*` is multiplication: 3 pizzas × 8 slices each = 24 slices
- `/` is division: 20 slices ÷ 4 people = 5 slices each
- `%` (modulo) is remainder: 10 ÷ 3 = 3 remainder **1**
- `**` is exponentiation: 2 to the power of 3 = 2 × 2 × 2 = 8

**Common Beginner Mistakes:**
- ❌ Forgetting `/` gives a **decimal** result: `5 / 2 = 2.5`, not `2`
- ❌ Using `/` when you meant `//` (floor division): `5 // 2 = 2` (drops the decimal)
- ❌ Confusing `%` with division: `10 % 3 = 1` (the remainder), not `3.33`

**Quick Memory Tip:**
`%` (modulo) = **remainder after division**. Most common use: checking if a number is even or odd: `if num % 2 == 0` means "even."

**Rule Example:**
```python
print(10 + 3)   # 13 (addition)
print(10 - 3)   # 7 (subtraction)
print(10 * 3)   # 30 (multiplication)
print(10 / 3)   # 3.333... (division—decimal result)
print(10 // 3)  # 3 (floor division—no decimal)
print(10 % 3)   # 1 (modulo—remainder)
print(10 ** 3)  # 1000 (exponentiation—10 to the power of 3)
```

---

### 4. **The print() Function (Python)**

**Simple Explanation:**
`print()` displays text or values on the screen. It's how Python talks to you.

**Real-World Analogy:**
Like shouting a message so everyone in the room can hear it.

**Common Beginner Mistakes:**
- ❌ Forgetting parentheses: `print "Hello"` ❌ (Python 3 requires parentheses)
- ❌ Not using quotes for text: `print Hello` ❌ (Python thinks "Hello" is a variable name)
- ❌ Using single quotes vs. double quotes inconsistently (both work the same in Python)

**Quick Memory Tip:**
Text goes **inside** the parentheses. String text needs **quotes**. Variables don't.

**Rule Example:**
```python
print("Hello")        # Prints: Hello
print(42)             # Prints: 42
name = "Daya"
print(name)           # Prints: Daya
print(name, "is", 20) # Prints: Daya is 20 (separated by spaces)
```

---

### 5. **F-Strings (Python)**

**Simple Explanation:**
An easy way to combine text and variables in one print statement. Use an `f` before the quotes and put variables in curly braces `{}`.

**Real-World Analogy:**
Like fill-in-the-blank sentences. The sentence stays the same, but you fill in the blanks with different names.

**Common Beginner Mistakes:**
- ❌ Forgetting the `f` before the quotes: `"{name}"` ❌ prints the literal text `{name}`, not the value
- ❌ Using single `{` or `}` instead of pairs
- ❌ Putting quotes around variable names inside `{}`

**Quick Memory Tip:**
**F-string formula**: `f"text {variable} more text"`. The `f` makes it an f-string. Variables go in `{}`.

**Rule Example:**
```python
name = "Daya"
age = 20
height = 5.9

# Without f-string (tedious):
print("My name is " + name + " and I am " + str(age) + " years old")

# With f-string (clean):
print(f"My name is {name} and I am {age} years old and my height is {height} ft")
# Prints: My name is Daya and I am 20 years old and my height is 5.9 ft
```

---

### 6. **HTML Document Structure**

**Simple Explanation:**
HTML is a **markup language** that tells browsers how to display content. Think of it as a **blueprint** for a webpage.

**Real-World Analogy:**
HTML is like the structure of a book:
- The whole book is wrapped in a book cover (`<html>`)
- Inside the book, the first page has the title and info (`<head>`)
- The next pages have the actual content (`<body>`)

**Common Beginner Mistakes:**
- ❌ Forgetting opening or closing tags: `<h1>Title</h1>` ✓ vs. `<h1>Title` ❌
- ❌ Not nesting tags correctly: `<h1><b>Title</h1></b>` ❌ should be `<h1><b>Title</b></h1>` ✓
- ❌ Not understanding that order matters in HTML (head comes before body)

**Quick Memory Tip:**
**Structure first, styling later.** HTML = structure. CSS = looks. JS = behavior.

**Rule Example:**
```html
<!DOCTYPE html>           <!-- Declares HTML5 -->
<html>                    <!-- Root element -->
  <head>                  <!-- Metadata & info -->
    <meta charset="UTF-8"> <!-- Allows special chars & emojis -->
    <title>Page Title</title>
  </head>
  <body>                  <!-- Visible content -->
    <h1>Main Heading</h1>
  </body>
</html>
```

---

### 7. **SQL & Databases**

**Simple Explanation:**
A **database** is an organized collection of data—like a digital filing system. **SQL** is the language you use to talk to databases: "Store this," "Show me that," "Delete this old stuff."

**Real-World Analogy:**
Imagine a huge library:
- The library = the database server (MySQL)
- Each bookshelf = a database (`onepiece_db`)
- Each book = a table (stores rows of data)
- Each page = a row of data
- Each line on the page = a column (field)

**Common Beginner Mistakes:**
- ❌ Forgetting the semicolon at the end of SQL commands
- ❌ Using `SELECT * FROM table WHERE x=5` without a semicolon
- ❌ Not understanding that `CREATE DATABASE` and `USE database` are separate steps

**Quick Memory Tip:**
**SQL workflow**: CREATE (make a database) → USE (enter it) → Query (ask for/add/delete data).

**Rule Example:**
```sql
CREATE DATABASE onepiece_db;  -- Create a new database
USE onepiece_db;              -- Enter the database
SELECT DATABASE();            -- Show which database you're in (prints: onepiece_db)
```

---

## File Inventory

| **File Name** | **Language** | **Purpose** | **Main Concepts** | **Status** |
|---|---|---|---|---|
| `index.html` | HTML | First webpage; introduces full-stack learning path | Document structure, meta tags, heading hierarchy | ✅ Complete |
| `practice.py` | Python | Variables, printing, arithmetic ops, mini exercises | Variables, data types, operators, f-strings, print() | ✅ Complete |
| `practice.sql` | SQL | Create database and verify connection | CREATE DATABASE, USE, SELECT DATABASE() | ✅ Complete |
| `README.md` | Markdown | Learning guide and reference (this file) | Structured documentation, link references | ✅ Complete |

---

## Code Explanations

### File 1: `index.html`

**Purpose:**
Your first HTML page—shows what you're learning on Days 1–90. It's a visual foundation.

**Concepts Used:**
- HTML5 document structure (`<!DOCTYPE>`, `<html>`, `<head>`, `<body>`)
- Meta tags for character encoding
- Heading tags for content hierarchy (`<h1>`, `<h2>`, `<h3>`)
- Document title

**Line-by-Line Explanation:**

```html
<!DOCTYPE html>
```
- Declares this is an **HTML5 document**. Every HTML file should start with this.
- Tells the browser how to interpret the file.

```html
<html>
```
- The **root element** that wraps everything.
- All HTML content goes inside this tag.

```html
<head>
```
- The **metadata section**—information *about* the page (not visible to users).
- Contains title, links to stylesheets, meta tags, JavaScript links, etc.

```html
<meta charset="UTF-8">
```
- **Character encoding** declaration.
- UTF-8 allows your page to display **emojis** 🎉, special characters, and text from any language.
- Without this, non-ASCII characters might display incorrectly.

```html
<title>My first day on html</title>
```
- Sets the **browser tab text** (what you see at the top of the browser window).
- Also used by search engines and bookmarks.

```html
</head>
<body>
```
- End of metadata section.
- Start of the **visible content section**.

```html
<h1>im learing html,css,jjs,react for frontend</h1>
```
- **Heading level 1** (most important, usually the page's main title).
- Text is large and bold by default.
- Should only appear once per page (best practice).

```html
<h2>and python for backend</h2>
<h3>Mysql for database</h3>
```
- **Heading level 2** and **3** (decreasing importance).
- Heading hierarchy helps with accessibility and SEO.

```html
</body>
</html>
```
- Closes the HTML structure.

**Inputs & Outputs:**
- **Input**: None (static HTML file)
- **Output**: A webpage with three headings displayed in the browser

**Important Logic:**
This file demonstrates the **minimum viable HTML page**. It has no styling (CSS) or interactivity (JavaScript)—just pure HTML structure.

---

### File 2: `practice.py`

**Purpose:**
Python fundamentals practice—variables, printing, arithmetic, simple calculations.

**Concepts Used:**
- `print()` function
- Variables and assignment
- Data types (string, int, float, bool)
- Arithmetic operators (`+`, `-`, `*`, `/`, `//`, `%`, `**`)
- F-strings
- Comments (single-line `#` and multi-line `"""..."""`)

**Block 1 — Introduction (Lines 1–8):**

```python
# Day 01 — Python Practice
print("Hello Fellow Learners")
print("this is day 1 in learning python")
```
- **`print()`**: Outputs text to the console.
- **`#` comment**: Explains the code. Comments are ignored by Python.
- **First run**: You'll see:
  ```
  Hello Fellow Learners
  this is day 1 in learning python
  ```

---

**Block 2 — Variables (Lines 11–17):**

```python
name="Daya"           # stores text
age="20"              # stores a number (but as text)
height=5.9            # stores a decimal
is_student=True       # stores True or False
```
- **Variables**: Named containers holding values.
- **Types present**:
  - `name`: string (text in quotes)
  - `age`: string (text in quotes—note: it's text "20", not number 20)
  - `height`: float (decimal number)
  - `is_student`: boolean (True/False)

```python
print(name)
print(age)
print(height)
print(f"My name is {name} and im {age} years old...")
```
- **`print()` with variables**: Outputs the variable's value, not its name.
- **F-string** `f"..."`: Lets you insert variables using `{variable}`.

**Output:**
```
Daya
20
5.9
My name is Daya and im 20 years old and my height is 5.9 ft and im a student
```

---

**Block 3 — Arithmetic Operators (Lines 22–29):**

```python
x=10
y=3
print("add=",x+y)             # 10 + 3 = 13
print("Sub=",x-y)             # 10 - 3 = 7
print("mul=",x*y)             # 10 * 3 = 30
print("div=",x/y)             # 10 / 3 = 3.333...
print("floor_div=",x+y)       # ⚠️ BUG: Should be x//y (currently prints x+y = 13)
print("mod=",x%y)             # 10 % 3 = 1 (remainder)
print("exponentiation=",x**y) # 10 ** 3 = 1000
```

**Operator Meanings:**
- `+`: Addition
- `-`: Subtraction
- `*`: Multiplication
- `/`: Division (always returns decimal, even if result is whole)
- `//`: Floor division (returns whole number, drops decimal)
- `%`: Modulo (returns remainder after division)
- `**`: Exponentiation (power)

**Note**: Line 27 has a bug—it should be `x//y` to demonstrate floor division, but it's `x+y`.

**Output:**
```
add= 13
Sub= 7
mul= 30
div= 3.3333...
floor_div= 13        # Bug: Should be 3 from 10//3
mod= 1
exponentiation= 1000
```

---

**Block 4 — Simple Exercises (Lines 31–43):**

```python
# Exercise: Mini calculator
price=100
width=30
final_price=price-width
print("final price=",final_price)
```
- **Purpose**: Show real-world use of arithmetic.
- **Logic**: Start with `price=100`, subtract `width=30` (discount?), result is `70`.
- **Output**: `final price= 70`

```python
# Exercise: Calculate rectangle area
length =10
width=5
area=length*width
print("Area:",area)
```
- **Purpose**: Practice multiplication with a common formula.
- **Logic**: Area = length × width = 10 × 5 = 50.
- **Formula**: `area = length × width`
- **Output**: `Area: 50`

---

**Full Execution Output:**
```
Hello Fellow Learners
this is day 1 in learning python
Daya
20
5.9
My name is Daya and im 20 years old and my height is 5.9 ft and im a student
add= 13
Sub= 7
mul= 30
div= 3.3333...
floor_div= 13
mod= 1
exponentiation= 1000
final price= 70
Area: 50
```

---

### File 3: `practice.sql`

**Purpose:**
SQL fundamentals—create a database, select it, verify connection.

**Concepts Used:**
- `CREATE DATABASE` statement
- `USE` statement
- `SELECT DATABASE()` function
- Comments (SQL uses `--` for single-line and `/* */` for multi-line)

**Explanation:**

```sql
-- Day 01 — SQL Practice
-- Topic: Install MySQL 8 + MySQL Workbench. Create first database...
```
- **SQL comments**: `--` marks a single-line comment (ignored by MySQL).
- Explains the lesson topic.

```sql
/*A database is like an Excel file. A table is like a sheet. 
SQL is the language you use to talk to it...*/
```
- **Multi-line comment** using `/* ... */`.
- Analogy: Database = Excel file, Table = Sheet, SQL = Language to query it.

```sql
create database onepiece_db;
```
- **`CREATE DATABASE`**: Creates a new database named `onepiece_db`.
- **Naming**: `onepiece_db` follows the convention: lowercase, underscore for spaces.
- **Semicolon**: `;` ends the SQL statement (required in most SQL contexts).

```sql
use onepiece_db;
```
- **`USE`**: Switches the current database to `onepiece_db`.
- After this, all subsequent SQL commands apply to this database.
- **Why needed**: MySQL server can have many databases; you must specify which one to use.

```sql
SELECT DATABASE();
```
- **`SELECT DATABASE()`**: A query that returns the name of the currently active database.
- **Output**: `onepiece_db` (displays in MySQL Workbench results panel).
- **Purpose**: Verification—confirms you're in the correct database.

---

**Execution Flow (in MySQL Workbench):**

1. Run line 1–2 (comments): Ignored.
2. Run line 3–4 (comments): Ignored.
3. Run `CREATE DATABASE onepiece_db;`:
   - **Result**: Database created. Message: "Query OK, 1 row affected."
4. Run `USE onepiece_db;`:
   - **Result**: Switched to database. Message: "Database changed."
5. Run `SELECT DATABASE();`:
   - **Result**: Shows `onepiece_db`. Output: 
     ```
     DATABASE()
     onepiece_db
     ```

---

## How to Run & Test

### Prerequisites

1. **HTML**: Any modern web browser (Chrome, Firefox, Safari, Edge)
2. **Python**: Python 3.11+ installed ([Download](https://www.python.org/downloads/))
3. **MySQL**: MySQL 8.0+ installed ([Download](https://dev.mysql.com/downloads/mysql/)) and MySQL Workbench ([Download](https://dev.mysql.com/downloads/workbench/))
4. **Code Editor**: VS Code with Python extension installed

### Running HTML

**Step 1:** Open `index.html` in a browser
- **Option A**: Right-click the file → "Open with" → Select your browser
- **Option B**: Double-click the file (opens in default browser)
- **Option C**: In VS Code, use the "Live Server" extension (right-click → "Open with Live Server")

**Expected Output:**
A webpage with three headings:
```
im learing html,css,jjs,react for frontend
and python for backend
Mysql for database
```

---

### Running Python

**Step 1:** Open terminal/command prompt  
**Step 2:** Navigate to the folder:
```bash
cd "c:\Users\murug\Downloads\Learn-FullStack-90Days\Day_01"
```

**Step 3:** Run the script:
```bash
python practice.py
```

**Expected Output:**
```
Hello Fellow Learners
this is day 1 in learning python
Daya
20
5.9
My name is Daya and im 20 years old and my height is 5.9 ft and im a student
add= 13
Sub= 7
mul= 30
div= 3.3333...
floor_div= 13
mod= 1
exponentiation= 1000
final price= 70
Area: 50
```

---

### Running SQL

**Step 1:** Open MySQL Workbench  
**Step 2:** Connect to your MySQL server (or create a connection)  
**Step 3:** Open `practice.sql` file in Workbench (File → Open SQL Script)  
**Step 4:** Run all queries:
- **Option A**: Click the "Execute All" button (lightning bolt ⚡)
- **Option B**: Select all text → Ctrl+Enter
- **Option C**: Highlight each line and Ctrl+Enter

**Expected Output:**
```
Query OK, 1 row affected.          (From CREATE DATABASE)
Database changed                    (From USE)
DATABASE()
onepiece_db                         (Result of SELECT DATABASE())
```

---

## Key Takeaways

1. **HTML structures content**: `<!DOCTYPE>`, `<head>`, `<body>`, heading tags (`<h1>`–`<h6>`) create a foundation for webpages.

2. **Variables store data**: Use variables to name and reuse values. Python allows `name = "Daya"` (string) or `age = 20` (integer).

3. **Data types matter**: Strings need quotes. Numbers don't. Booleans are `True`/`False`. Choose the right type for your data.

4. **Arithmetic operators do math**: `+`, `-`, `*`, `/`, `//`, `%`, `**` let you perform calculations. `/` gives decimals; `//` drops decimals.

5. **print() shows output**: Use `print()` to display text or variables. F-strings (`f"...{var}..."`) make it easy to mix text and variables.

6. **Databases organize data**: `CREATE DATABASE` and `USE` let you create and select databases. `SELECT DATABASE()` verifies your location.

7. **SQL is a language**: Like Python, SQL has syntax rules. Most SQL statements end with `;`.

8. **The three-layer architecture**: Frontend (HTML) displays, Backend (Python) processes, Database (MySQL) stores. Day 1 touches all three.

9. **Modulo (%) finds remainders**: `10 % 3 = 1`. Most common use: `if x % 2 == 0` checks if a number is even.

10. **Consistency is key**: Use meaningful variable names, proper indentation, and comments. Future you (and teammates) will thank you.

---

## Practice Tasks

### Easy

1. **Modify the HTML**: Add a fourth heading (`<h4>`) that says "and React for frontend framework" below the `<h3>`.
   - **Goal**: Understand heading hierarchy and nesting.

2. **Create a personal summary in Python**: Write a script that creates 5 variables for your own data (name, age, height, city, hobby) and prints a summary using an f-string.
   - **Example output**: "I am [name], [age] years old, [height]ft tall, from [city], and I love [hobby]."
   - **Goal**: Practice variables and f-strings.

3. **Arithmetic puzzle**: Calculate the total cost of 3 items: item1 = $25, item2 = $18, item3 = $42. Add tax (10%). Print the final total.
   - **Goal**: Practice operators and math.

---

### Medium

4. **HTML with content**: Create a new HTML page called `profile.html` that displays:
   - A heading "My Profile"
   - Your name in a paragraph
   - A list of 3 things you want to learn (use heading tags or lists)
   - **Goal**: Practice HTML structure and organization.

5. **Python calculation**: Write Python code that:
   - Takes a price
   - Calculates a 15% discount
   - Calculates 8% tax on the discounted price
   - Shows the original price, discount amount, tax amount, and final price
   - **Goal**: Practice multi-step calculations and variable reuse.

6. **Check even/odd**: Write Python code that uses the modulo operator to check if 5 numbers (17, 24, 13, 88, 5) are even or odd.
   - **Goal**: Understand modulo and conditionals (simple if-else).

---

### Hard

7. **SQL exploration**: Create a database called `student_learning_db`. Then:
   - Create a table called `progress` (you'll learn table syntax later, but research it)
   - Insert a row: `name = "Daya"`, `day_completed = 1`, `status = "in_progress"`
   - Select all rows from the table
   - **Goal**: Preview what's coming in future days (databases are not just about creation).

8. **Full-stack mini project**: Create a Python script called `calculator.py` that:
   - Asks for 3 expenses (food, transport, entertainment)
   - Calculates total
   - Calculates percentage each represents of the total
   - Saves results to print in an HTML file (bonus: actually creates an HTML file dynamically)
   - **Goal**: Combine Python + arithmetic + understanding output format.

9. **Explain in your own words**: Write a markdown file (`EXPLANATION.md`) in Day_01 that explains:
   - Why we need three separate layers (HTML, Python, SQL) instead of one
   - What each layer does and why it matters
   - One real-world example of a full-stack app (e.g., Instagram, Amazon, Twitter)
   - **Goal**: Deepen understanding through teaching others.

---

## FAQ

### Q1: Do I need to write code exactly as shown?
**A:** No! Use the examples as guides. Variable names, text content, and specific numbers can change. The **principles** (structure, logic, syntax rules) are what matter.

---

### Q2: Why is my Python script not running?
**Common causes:**
- **Not in the correct directory**: Use `cd` to navigate to the Day_01 folder.
- **Python not installed**: Check with `python --version`. Install from [python.org](https://www.python.org) if missing.
- **File name typo**: Make sure the file is named `practice.py` (not `Practice.py` or `practice.txt`).
- **Syntax error**: Check for missing colons, quotes, or parentheses.

---

### Q3: What's the difference between `/` and `//` in Python?
**A:**
- `/` divides and returns a decimal: `10 / 3 = 3.3333...`
- `//` divides and drops the decimal (floor division): `10 // 3 = 3`

Use `/` when you need exact division. Use `//` when you need whole numbers only.

---

### Q4: Why do strings need quotes but numbers don't?
**A:** Python uses quotes to mark text. Without quotes, Python thinks `20` is the number twenty. With quotes, `"20"` is the text-string "twenty," which behaves differently:
- `20 + 5 = 25` (math)
- `"20" + "5" = "205"` (text concatenation, if using `+`)

---

### Q5: What's the difference between `<h1>`, `<h2>`, and `<h3>`?
**A:** They're **heading levels**:
- `<h1>` = Most important (should appear once per page)
- `<h2>` = Subheading
- `<h3>` = Sub-subheading
- ... up to `<h6>`

They communicate **hierarchy** to browsers and search engines. Larger numbers = less important.

---

### Q6: Why do SQL statements end with a semicolon?
**A:** The semicolon tells MySQL "I'm done with this command; execute it." Without it, MySQL waits for more input. Some tools (like MySQL Workbench) execute anyway, but it's required in real applications.

---

### Q7: Is it normal to feel confused on Day 1?
**A:** **Yes!** You're meeting three new languages and a new workflow. By Day 90, this will feel natural. Focus on understanding the **core ideas** (variables, print, database creation), not memorizing syntax. Repetition builds mastery.

---

### Q8: Can I run multiple SQL statements at once?
**A:** Yes! In MySQL Workbench, select all the code and press Ctrl+Enter. Each statement (ending with `;`) executes separately. Results appear in order.

---

### Q9: What does "meta charset" actually do?
**A:** It tells the browser which character **encoding** to use. UTF-8 is the universal standard that handles English, emojis 🎉, Chinese characters 中文, Arabic العربية, and almost every language. Without it, you might see question marks ? instead of special characters.

---

### Q10: Should I memorize all the operators now?
**A:** No. Memorize the **main ones** (`+`, `-`, `*`, `/`, `%`). Others like `**` will become natural with practice. Refer back to this README when needed—that's what documentation is for!

---

## Summary

**Day 1 is your onboarding day.** You've set up three separate environments (HTML file, Python script, MySQL database) and understand how they fit together:

- **Frontend (HTML)**: Displays the user interface—what people see in their browser
- **Backend (Python)**: Processes logic and calculations—the "brains" of the application
- **Database (MySQL)**: Stores persistent data—the "memory" of the application

You've learned foundational concepts in each layer: HTML structure, Python variables and operators, SQL database creation. You've run code and seen output. Most importantly, you've realized that **full-stack development is a three-layer system**, and each layer has its own language and purpose.

**Your mission for the next 89 days**: Go deeper into each layer. Day by day, you'll build complex projects that combine all three. By Day 90, you'll have gone from "Hello, World!" to building real, production-grade full-stack applications.

---

## Quick Reference Card

| **Layer** | **Language** | **Purpose** | **Key Concept** |
|---|---|---|---|
| Frontend | HTML | Display info to users | Structure & semantics |
| Backend | Python | Process logic & calculations | Variables & operators |
| Database | SQL | Store persistent data | Databases & tables |

| **Python Basics** | **Example** |
|---|---|
| Create variable | `name = "Daya"` |
| Print output | `print(name)` |
| Arithmetic | `result = 10 + 5` |
| F-string | `f"Hello {name}"` |
| Modulo (remainder) | `10 % 3 = 1` |

| **HTML Basics** | **Purpose** |
|---|---|
| `<!DOCTYPE html>` | Declares HTML5 |
| `<head>` | Metadata & info |
| `<body>` | Visible content |
| `<h1>` ... `<h6>` | Headings (hierarchy) |
| `<meta charset="UTF-8">` | Character encoding |

| **SQL Basics** | **Command** |
|---|---|
| Create database | `CREATE DATABASE name;` |
| Enter database | `USE name;` |
| Check current database | `SELECT DATABASE();` |

---

**Happy coding! 🚀 See you on Day 2!**
## Next Day

Continue to [Day 02](../Day_02/README.md) for the next step in the learning path.