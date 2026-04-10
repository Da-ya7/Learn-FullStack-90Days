# Day 02 Learning README

[![Day 02](https://img.shields.io/badge/Day-02-0f766e?style=for-the-badge)](https://github.com/)
[![HTML5](https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white)](https://developer.mozilla.org/en-US/docs/Web/HTML)
[![Python](https://img.shields.io/badge/Python-3.13%2B-3776ab?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![MySQL](https://img.shields.io/badge/MySQL-8.0-4479a1?style=for-the-badge&logo=mysql&logoColor=white)](https://dev.mysql.com/)
[![Status](https://img.shields.io/badge/Status-Active_Learning-f59e0b?style=for-the-badge)]()
[![Learning Focus](https://img.shields.io/badge/Focus-Data%20Types%20%26%20Input-8b5cf6?style=for-the-badge)]()
[![Last Updated](https://img.shields.io/badge/Updated-2026--04--10-gray?style=for-the-badge)]()

---

## 📚 Table of Contents

1. [Day Overview](#day-overview)
2. [What Was Built](#what-was-built)
3. [What Was Learned](#what-was-learned)
4. [Why This Day Matters](#why-this-day-matters)
5. [Concepts Explained Simply](#concepts-explained-simply)
6. [File Inventory](#file-inventory)
7. [Code Explanation](#code-explanation-file-by-file)
8. [How to Run or Test](#how-to-run-or-test)
9. [Key Takeaways](#key-takeaways)
10. [Practice Tasks](#practice-tasks)
11. [FAQ](#faq)
12. [Summary](#summary)

---

## 🎯 Day Overview

### What Was Built

Day 02 is a **three-language deep dive into data types and user interaction**:

- **HTML**: Built a personal portfolio page showcasing text formatting, semantic tags, and inline styling
- **Python**: Created programs that accept user input and perform type conversions
- **SQL**: Designed a database table and learned how to insert and retrieve data

This day bridges the gap between static content and dynamic, interactive applications.

### What Was Learned

- How different programming languages classify and handle data
- Why converting data types matters (and how it crashes your code if you don't)
- How to structure data in databases using proper types
- How to ask users for information and use it in your programs
- The hidden difference between nothing (`NULL`) and blank (`""`)

### Why This Day Matters

**Data is everything in programming.** Before you can build anything useful, you need to:

1. **Understand** what type of data you're working with
2. **Convert** data from one type to another safely
3. **Store** data with proper structure (SQL)
4. **Accept** user input without crashing

Day 02 teaches you these fundamentals across all three stacks. Without mastering this, you'll spend hours debugging simple issues like "why is 5 + 5 equal to 55?" (because they're strings, not numbers!).

---

## 💡 Concepts Explained Simply

### Concept 1: Data Types

**Simple Explanation**

A data type is a category that tells your computer what kind of information to expect. Just like a mailbox labeled "bills" is for bills and not groceries, a variable labeled `int` is for whole numbers and not text.

**Real-World Analogy**

Imagine a restaurant order form:
- **Name field** → text (string) - "John Smith"
- **Quantity field** → whole numbers (int) - 5
- **Price field** → decimal numbers (float) - 19.99
- **Is VIP?** → yes/no (boolean) - True or False

If someone writes "five" in the quantity field instead of 5, the kitchen knows there's a problem.

**Common Beginner Mistakes**

1. Treating `"123"` and `123` the same way (they're not!)
2. Trying to add a string and a number: `"5" + 5` → **CRASH**
3. Assuming `NULL` is the same as `""` (empty string)
4. Not converting input before doing math

**Quick Memory Tip**

> Numbers for math, strings for words, booleans for yes/no, decimals for money.

### Concept 2: Type Conversion (Casting)

**Simple Explanation**

Type conversion is the process of changing data from one type to another. When users type something, your program receives it as text. You need to convert it to a number if you want to do math.

**Real-World Analogy**

Converting currency. You have 100 dollars, but you need euros. You don't have euros yet—you have dollars. You must exchange them at a conversion rate. The same data (money), different format.

**Common Beginner Mistakes**

1. Forgetting to convert: `int(input("Age: ")) + 5` works, but `input("Age: ") + 5` crashes
2. Converting wrong: `int("5.5")` crashes (you need `float("5.5")` first, then `int()`)
3. Assuming conversion is perfect: `int(9.8)` gives 9 (NOT 10—decimals are cut off, not rounded)

**Quick Memory Tip**

> **Every input is a string first.** Convert it before you use it.

### Concept 3: User Input

**Simple Explanation**

The `input()` function pauses your program and waits for the user to type something. Whatever they type comes back as a string, no matter what.

**Real-World Analogy**

You ask a customer "How old are you?" They say "25". That's text they spoke. If you want to use 25 in math, you need to understand it's a number, not just words.

**Common Beginner Mistakes**

1. Forgetting to store the input: `input("Name: ")` runs but does nothing
2. Using input result directly in math: `input("Number: ") * 5` gives repeated strings, not multiplication
3. Assuming the user will always enter valid data (they won't!)

**Quick Memory Tip**

> **Store it, convert it, use it.** Three steps, every time.

### Concept 4: NULL vs Empty String (SQL Focus)

**Simple Explanation**

- **NULL** = "This value doesn't exist. The data is missing entirely."
- **Empty string `""`** = "The value exists, but it's blank."

**Real-World Analogy**

- **NULL** = A student never submitted the assignment (missing)
- **Empty string** = A student submitted a blank paper (present but empty)

**Common Beginner Mistakes**

1. Using `WHERE crew_name = NULL` instead of `WHERE crew_name IS NULL`
2. Treating empty and NULL the same way in queries
3. Not understanding why your WHERE clause doesn't match rows with NULL

**Quick Memory Tip**

> **NULL = missing. Use IS NULL. Empty = blank text. Use = ""**

### Concept 5: SQL Query Reading

**Simple Explanation**

Read SQL queries like English from left to right.

**Example**

```sql
SELECT name, age FROM characters WHERE age > 20;
```

Read as: "Give me the **name and age** FROM **the characters table** WHERE **age is greater than 20**."

---

## 📊 File Inventory

| File Name | Language | Purpose | Main Concepts |
|-----------|----------|---------|----------------|
| `practice.py` | Python | Learn data types and user input | `int`, `float`, `str`, `bool`, type conversion, `input()` |
| `practice.sql` | SQL | Learn table structure and queries | `CREATE TABLE`, `INSERT`, `SELECT`, `WHERE`, `NULL` |
| `index.html` | HTML | Build a personal page with text formatting | Semantic tags, inline styles, text decoration |

---

## 🔍 Code Explanation (File by File)

---

### 📄 File: `practice.py`

**Purpose**

This Python file teaches the four foundations: data types, printing types, type conversion, and user input. It's a hands-on exploration of how Python handles information.

**Concepts Used**

- Data types: `int`, `float`, `str`, `bool`
- Type checking with `type()`
- Type conversion: `int()`, `str()`, `float()`
- User input with `input()`
- F-strings for formatted output

---

#### **Block 1: Defining Data Types (Lines 3-6)**

```python
age = 20                #int=whole number
price = 99.99           #float number with decimal
name = "Dhayalan"       #text wrapped in quotes
is_active = True        #boolean: True or False
```

**What It Does**

Creates four variables, each holding a different type of data. This mirrors how real programs store information.

**Explanation**

- `age = 20` → Stores a whole number
- `price = 99.99` → Stores a decimal number
- `name = "Dhayalan"` → Stores text (strings always have quotes)
- `is_active = True` → Stores a yes/no value

**Important Logic Decision**

The code stores each type separately to demonstrate Python's flexibility. You can put any type in any variable, but the type doesn't change unless you explicitly convert it.

---

#### **Block 2: Printing Data Types (Lines 8-11)**

```python
print(type(age))        # <class 'int'>
print(type(price))      # <class 'float'>
print(type(name))       # <class 'str'>
print(type(is_active))  # <class 'bool'>
```

**What It Does**

Uses the built-in `type()` function to inspect what category each variable belongs to.

**Explanation**

`type()` is Python's detective tool. It looks at a variable and tells you its category. This is useful when you think something is a number but it's actually text.

---

#### **Block 3: String to Integer Conversion (Lines 15-20)**

```python
age_str = "20"          # This is text, not a number
age_int = int(age_str)  # Convert text to integer
print(type(age_str))    # <class 'str'>
print(type(age_int))    # <class 'int'>
print(age_int + 5)      # 25 ✓ Works: 20 + 5
print(age_str + "5")    # "205" ✓ String concatenation, not math
```

**What It Does**

Demonstrates the critical difference between `"20"` (text) and `20` (number).

**Explanation**

- Line 1: `"20"` is two characters, not a number
- Line 2: `int("20")` converts the text to a real integer
- Line 5: `20 + 5 = 25` ✓ Math works with integers
- Line 6: `"20" + "5" = "205"` ✗ Strings concatenate, not add

**Common Beginner Mistake**

Students often try: `print("20" + 5)` and get an error. Python refuses because text and numbers can't mix.

---

#### **Block 4: Integer to String Conversion (Lines 22-24)**

```python
score = 100
message = "Your score: " + str(score)
print(message)  # Your score: 100
```

**What It Does**

Converts a number to text so it can be joined with a string.

**Explanation**

- `score = 100` is a number
- `str(score)` converts it to the text `"100"`
- `"Your score: " + "100"` combines them into one message

This is how programs display results to users: they convert numbers to text and display them.

---

#### **Block 5: Other Conversions (Lines 26-30)**

```python
x = 5
print(float(x))     # 5.0 (integer to decimal)

y = 9.8
print(int(y))       # 9 (decimal to integer — cuts off decimal, doesn't round)
```

**What It Does**

Shows conversions between float and int.

**Explanation**

- `float(5)` → `5.0` (adds decimal point, same value)
- `int(9.8)` → `9` (removes decimal part, doesn't round to 10)

**Important Logic Decision**

`int()` truncates (cuts off) rather than rounds. If you want 9.8 to become 10, you must use `round(9.8)` instead.

---

#### **Block 6: Getting User Input (Lines 35-40)**

```python
name = input("Enter your name: ")
print(f"hello {name}")

age = int(input("enter your age: "))
print(f"your age is {age}")

height = float(input("Enter your height in cm: "))
print(f"your height is {height}")
```

**What It Does**

Pauses the program to let users type information, then uses that information.

**Explanation**

- `input("prompt")` displays a question and waits
- Everything from `input()` is a string, even if the user types numbers
- Line 2: Takes the text the user typed and uses it in an f-string
- Line 4: Converts input to a number before storing
- Line 7: Converts input to a decimal number

**Important Logic Decision**

Notice line 4 and 7 use conversion immediately: `int(input(...))`. This ensures the program gets a number, not text.

If you wrote `age = input(...)` then `print(age + 5)`, you'd get an error because Python can't add strings and numbers.

---

#### **Block 7: Practice Program (Lines 42-48)**

```python
your_name = input("Enter your name: ")
birth_year = int(input("Enter your birth year: "))
age = 2025 - birth_year
print(f"Your name is {your_name} and your approximate age is {age}")
```

**What It Does**

A complete program that asks for user input, does math, and displays a result.

**Explanation**

1. Line 1: Gets the user's name as text
2. Line 2: Gets birth year as text, converts to integer
3. Line 3: Subtracts birth year from 2025 to calculate age
4. Line 4: Displays everything in a formatted message

**Inputs and Outputs**

| Input | Expected Output |
|-------|-----------------|
| Name: "Alice", Birth Year: "2005" | "Your name is Alice and your approximate age is 20" |
| Name: "Bob", Birth Year: "1990" | "Your name is Bob and your approximate age is 35" |

---

### 📊 File: `practice.sql`

**Purpose**

This SQL file teaches how databases work: you define the structure (table with columns and types), add data (INSERT), and retrieve it (SELECT). It uses a One Piece theme to make it memorable.

**Concepts Used**

- SQL data types: `INT`, `VARCHAR(n)`, `TEXT`, `DECIMAL`, `DATE`, `BOOLEAN`
- `CREATE TABLE` to define structure
- `INSERT INTO` to add rows
- `SELECT` to retrieve data
- `WHERE` to filter rows
- `NULL` vs empty values
- Comparison operators: `=`, `>`, `IS NULL`

---

#### **Block 1: Understanding SQL Data Types (Lines 1-11)**

```sql
-- Data types in SQL
-- int - whole numbers - ex:age,id,etc..
-- VARCHAR(n) - Text up to n characters - ex:name VARCHAR(50)
-- TEXT - Long text, no limit - description, bio
-- DECIMAL(p,s) - Precise decimals - price DECIMAL(10,2)
-- DATE - A date: - YYYY-MM-DD - 2025-01-15
-- BOOLEAN - True (1) or False (0) - is_active
```

**What It Does**

Lists the seven main data types in SQL with real-world use cases.

**Explanation by Type**

| Type | Use Case | Example |
|------|----------|---------|
| `INT` | Whole numbers | age `INT`, user_id `INT` |
| `VARCHAR(50)` | Short text with a limit | name `VARCHAR(50)` (max 50 characters) |
| `TEXT` | Long text, no limit | description `TEXT` |
| `DECIMAL(10,2)` | Money and precise decimals | price `DECIMAL(10,2)` (10 digits total, 2 after decimal) |
| `DATE` | Dates only | birth_date `DATE` (format: YYYY-MM-DD) |
| `BOOLEAN` | True or false | is_active `BOOLEAN` |

**Why This Matters**

Choosing the right type prevents errors and saves space. If you store age as `TEXT`, then `age > 20` fails because you can't compare text with numbers.

---

#### **Block 2: Creating Your First Table (Lines 18-23)**

```sql
USE onepiece_db;

CREATE TABLE characters(
    name varchar(50),
    age int,
    crew_name text
);
```

**What It Does**

Creates an empty table called `characters` with three columns: name, age, and crew_name.

**Explanation**

- `USE onepiece_db;` → Tells SQL which database to use
- `CREATE TABLE characters(...)` → Creates a new table named `characters`
- `name varchar(50)` → Column 1: text up to 50 characters
- `age int` → Column 2: whole numbers only
- `crew_name text` → Column 3: long text, no limit

**Important Logic Decision**

At this point, the table is empty. No data exists yet. It's like an empty spreadsheet with column headers but no rows.

---

#### **Block 3: Inserting Data (Lines 25-35)**

```sql
INSERT INTO characters (name, age, crew_name)
VALUES ('luffy', 19, 'Straw_hat');

INSERT INTO characters (name, age, crew_name)
VALUES ('Z0r0', 22, 'Straw hat');

INSERT INTO characters (name, age, crew_name)
VALUES ('Sanji', 22, 'Straw hat');
```

**What It Does**

Adds three rows (characters) to the empty table.

**Explanation**

Each `INSERT` statement:
1. Names the table: `INTO characters`
2. Lists the columns: `(name, age, crew_name)`
3. Provides matching values: `VALUES ('luffy', 19, 'Straw_hat')`

Text values use single quotes: `'luffy'`  
Numbers don't: `19`

**Inputs and Outputs**

After these three INSERTs, the table looks like:

| name | age | crew_name |
|------|-----|-----------|
| luffy | 19 | Straw_hat |
| Z0r0 | 22 | Straw hat |
| Sanji | 22 | Straw hat |

---

#### **Block 4: Selecting All Data (Lines 37-39)**

```sql
SELECT * from characters;  -- Select all rows and columns
SELECT name, crew_name from characters;  -- Select specific columns
```

**What It Does**

Retrieves data from the table.

**Explanation**

- `SELECT *` → Get every column from the table
- `SELECT name, crew_name` → Get only these two columns
- `FROM characters` → From this specific table

**Output of First Query**

```
name   age  crew_name
luffy  19   Straw_hat
Z0r0   22   Straw hat
Sanji  22   Straw hat
```

**Output of Second Query**

```
name   crew_name
luffy  Straw_hat
Z0r0   Straw hat
Sanji  Straw hat
```

Notice: Age column is missing in the second query because we didn't ask for it.

---

#### **Block 5: Filtering with WHERE (Lines 41-43)**

```sql
SELECT * FROM characters WHERE age > 20;
SELECT * FROM characters WHERE name = 'Luffy';
```

**What It Does**

Returns only rows that match a condition.

**Explanation**

- `WHERE age > 20` → Only rows where age is greater than 20
- `WHERE name = 'Luffy'` → Only rows where name equals 'Luffy'

**Query 1 Output** (age > 20)

```
name   age  crew_name
Z0r0   22   Straw hat
Sanji  22   Straw hat
```

**Query 2 Output** (name = 'Luffy')

```
name   age  crew_name
luffy  19   Straw_hat
```

**Important Logic Decision**

Without `WHERE`, you get all rows. With `WHERE`, you filter. This is how you find specific data in huge tables.

---

#### **Block 6: Understanding NULL (Lines 50-57)**

```sql
-- NULL means "no value at all — the data is missing"
-- Empty string "" means "the value exists, but it's blank"

INSERT INTO characters (name, age, crew_name)
VALUES ('Garp', 72, NULL);

SELECT * FROM characters WHERE crew_name IS NULL;
-- Note: WHERE crew_name = NULL does NOT work — always use IS NULL
```

**What It Does**

Introduces NULL and demonstrates the correct way to find NULL values.

**Explanation**

- `NULL` → Missing value (empty cell in a spreadsheet)
- `""` → Blank text (a cell with an empty string)
- `IS NULL` → The correct way to find missing values
- `= NULL` → **Wrong.** This never works. Always use `IS NULL`.

**Why NULL Exists**

Imagine a "crew_name" column. What if a character hasn't joined a crew yet? Options:
1. Leave it blank: `""`  (but this is still a value, just empty)
2. Mark it NULL: `NULL` (meaning "I don't know" or "not applicable")

**Common Beginner Mistake**

```sql
-- WRONG ❌
SELECT * FROM characters WHERE crew_name = NULL;

-- CORRECT ✓
SELECT * FROM characters WHERE crew_name IS NULL;
```

The first query returns no results because `NULL` can't be compared with `=`. You must use `IS NULL`.

---

### 🎨 File: `index.html`

**Purpose**

This HTML file demonstrates text formatting, semantic tags, and inline styling. It's a personal portfolio page that shows who you are and what you're learning.

**Concepts Used**

- Semantic text tags: `<strong>`, `<em>`, `<cite>`, `<mark>`, `<del>`, `<ins>`
- Structural formatting: `<sup>`, `<sub>`, `<blockquote>`
- Inline CSS styling: `style` attribute
- Meta charset for special characters
- Image embedding with `<img>`

**Structure Overview**

The HTML is organized into:
1. Meta information (charset)
2. Headings with centered, colored text
3. Personal introduction paragraph
4. Educational content with special formatting
5. Reference section with blockquote
6. Image of favorite character

---

#### **Block 1: HTML Head Section (Lines 1-4)**

```html
<head>
    <meta charset="UTF-8">
    <title>Second day on html</title>
</head>
```

**What It Does**

Sets up the page with meta information and a title.

**Explanation**

- `<meta charset="UTF-8">` → Tells the browser to use UTF-8 encoding, which allows emojis, accented characters, and special symbols to display correctly
- `<title>Second day on html</title>` → The page title shown in the browser tab

**Why It Matters**

Without `charset="UTF-8"`, special characters might display as garbled text: `â„¢` instead of `™`

---

#### **Block 2: Headings with Inline Styling (Lines 8-11)**

```html
<h1 style="text-align: center; color: purple;">Main heading</h1>
<h2 style="text-align: center; color: lightblue;">Second Main heading</h2>
<h3 style="text-align: center; color: blue;">Sub heading</h3>
```

**What It Does**

Creates a three-level heading hierarchy with centered, colored text.

**Explanation**

- `<h1>`, `<h2>`, `<h3>` → Heading levels (1 is biggest, 3 is smaller)
- `style="text-align: center;"` → Center the text horizontally
- `color: purple;` → Make the text purple
- Inline `style` attribute → Quick way to style single elements (not recommended for large projects, but fine for learning)

**Semantic Importance**

Headings create hierarchy. Screen readers and search engines use them to understand page structure.

---

#### **Block 3: Personal Introduction (Lines 14-18)**

```html
<p style="text-align: center;">
  <strong><em>My name is Dhayalan</em></strong>,
  <em>I'm a final year B.E student.</em><br>
  Hope this GitHub is useful to you. You can also contribute to this repository.
</p>
```

**What It Does**

Introduces the person with emphasis and text formatting.

**Explanation by Tag**

| Tag | Purpose | Semantic Meaning |
|-----|---------|------------------|
| `<strong>` | Makes text bold | High importance |
| `<em>` | Makes text italic | Emphasis/stress |
| `<br>` | Line break | Forces a new line |

**Example Output**

```
***My name is Dhayalan***, I'm a final year B.E student.
Hope this GitHub is useful to you. You can also contribute to this repository.
```

(The text "My name is Dhayalan" is bold AND italic because both tags wrap it)

**Important Logic Decision**

`<strong>` and `<em>` are semantic tags—they mean something. They're not just for styling:
- `<strong>` means "this is important"
- `<em>` means "this deserves emphasis in reading"
- Use them for meaning, not just looks

---

#### **Block 4: Superscript, Subscript, and Special Formatting (Lines 19-21)**

```html
<p style="text-align: center;">
  while studying E=MC<sup>2</sup>. I drink H<sub>2</sub>O.<br>
  After finish studying i started watching <mark>ONE-PIECE</mark>, 
  And my favorite character is <del>Luffy</del> <ins><cite>Monkey D Luffy</ins>
</p>
```

**What It Does**

Uses advanced text formatting for scientific notation, highlighting, and redaction.

**Explanation by Tag**

| Tag | Purpose | Output | Use Case |
|-----|---------|--------|----------|
| `<sup>` | Superscript | E=MC² | Exponents, footnotes |
| `<sub>` | Subscript | H₂O | Chemical formulas, indices |
| `<mark>` | Highlight | ONE-PIECE (yellow background) | Mark important text |
| `<del>` | Struck through | ~~Luffy~~ | Show removed content |
| `<ins>` | Underlined insertion | Monkey D Luffy (underlined) | Show added content |
| `<cite>` | Citation/title style | Special formatting | Reference works/titles |

**Visual Example**

```
E=MC² and H₂O are displayed correctly with superscript and subscript.
ONE-PIECE is highlighted in yellow.
Luffy is struck through, replaced with Monkey D Luffy (underlined).
```

---

#### **Block 5: Blockquote Section (Lines 22-25)**

```html
<blockquote style="text-align:center;">
  w3school has the best tutorials for html...
  [... rest of text ...]
</blockquote>
```

**What It Does**

Displays a longer quote with visual indentation and styling.

**Explanation**

- `<blockquote>` → Semantic tag for quotes/references
- Creates visual indentation on both sides
- Usually italicized by default browser styling
- `style="text-align:center;"` → Center the quote text

**Semantic Importance**

Tells screen readers and search engines: "This is a quotation or reference."

---

#### **Block 6: Image Embedding (Lines 26-28)**

```html
<p style="text-align: center;">
  <img src="https://encrypted-tbn0.gstatic.com/images?q=..." alt="Luffy">
</p>
```

**What It Does**

Displays an image of the favorite character.

**Explanation**

- `<img>` → Image element (no closing tag)
- `src="..."` → The web address (URL) where the image lives
- `alt="Luffy"` → Alternative text if image fails to load (also helps screen readers and SEO)

**Important Logic Decision**

Always include `alt` text. If the image doesn't load, users still understand what was there. Plus, it helps accessibility for people using screen readers.

---

## 🚀 How to Run or Test

### Prerequisites

- **Python**: Version 3.7 or higher
  - Check: `python --version` or `python3 --version`
  
- **MySQL**: Version 8.0 or higher
  - Check: `mysql --version`
  - Ensure MySQL server is running
  
- **Text Editor or IDE**: VS Code, PyCharm, or any text editor
  
- **Modern Web Browser**: Chrome, Firefox, Safari, or Edge for HTML

---

### Running Python (`practice.py`)

#### **Step 1: Navigate to Day 2**

```bash
cd c:\Users\murug\Downloads\Learn-FullStack-90Days\Day_02
```

#### **Step 2: Run the Script**

```bash
python practice.py
```

or

```bash
python3 practice.py
```

#### **Expected Output**

```
<class 'int'>
<class 'float'>
<class 'str'>
<class 'bool'>
<class 'str'>
<class 'int'>
25
205
Your score: 100
5.0
9
Enter your name: [waits for input]
```

The program will pause at each `input()` call and wait for you to type something.

#### **Sample Interactive Session**

```
Enter your name: Alice
hello Alice
enter your age: 25
your age is 25
Enter your height in cm: 165.5
your height is 165.5
```

---

### Running SQL (`practice.sql`)

#### **Step 1: Connect to MySQL**

```bash
mysql -u root -p
```

(Enter your MySQL password when prompted)

#### **Step 2: Copy Each Query**

Open `practice.sql` and copy each query block into the MySQL terminal.

**Example: Create Table**

```sql
USE onepiece_db;

CREATE TABLE characters(
    name varchar(50),
    age int,
    crew_name text
);
```

Then press Enter. Expected response: `Query OK, 0 rows affected`

**Example: Insert Data**

```sql
INSERT INTO characters (name, age, crew_name)
VALUES ('luffy', 19, 'Straw_hat');
```

Expected response: `Query OK, 1 row affected`

**Example: Select and View**

```sql
SELECT * FROM characters;
```

Expected output:

```
+------+-----+-----------+
| name | age | crew_name |
+------+-----+-----------+
| luffy | 19 | Straw_hat |
+------+-----+-----------+
```

#### **All Practice Queries in Sequence**

```sql
USE onepiece_db;
CREATE TABLE characters(name varchar(50), age int, crew_name text);
INSERT INTO characters (name, age, crew_name) VALUES ('luffy', 19, 'Straw_hat');
INSERT INTO characters (name, age, crew_name) VALUES ('Z0r0', 22, 'Straw hat');
INSERT INTO characters (name, age, crew_name) VALUES ('Sanji', 22, 'Straw hat');
SELECT * FROM characters;
SELECT name, crew_name FROM characters;
SELECT * FROM characters WHERE age > 20;
SELECT * FROM characters WHERE name = 'Luffy';
INSERT INTO characters (name, age, crew_name) VALUES ('Garp', 72, NULL);
SELECT * FROM characters WHERE crew_name IS NULL;
```

---

### Opening HTML (`index.html`)

#### **Step 1: Navigate to Day 2**

```bash
cd c:\Users\murug\Downloads\Learn-FullStack-90Days\Day_02
```

#### **Step 2: Open in a Browser**

Double-click `index.html` or right-click → "Open with" → Choose your browser.

#### **Expected Display**

- Purple "Main heading" centered at top
- Light blue "Second Main heading" below it
- Blue "Sub heading" below that
- Personal introduction text, centered
- Scientific notation: E=MC² and H₂O
- Yellow-highlighted "ONE-PIECE"
- Struck-through "Luffy" replaced with underlined "Monkey D Luffy"
- W3Schools reference quote in centered blockquote
- Character image (Luffy) displaying below

---

## 🎯 Key Takeaways

1. **Data Types Are Categories** — Every piece of data belongs to a type. `"5"` and `5` look similar but behave completely differently.

2. **Conversion Is Critical** — Every time a user types something, it's text. Convert it to a number before you do math with it.

3. **NULL ≠ Empty** — `NULL` means missing data. `""` means blank text. Know the difference; search correctly with `IS NULL`.

4. **SQL Queries Are English** — Read SQL left-to-right like sentences. `SELECT name FROM characters WHERE age > 20` = "Give me names where age exceeds 20."

5. **HTML Semantics Matter** — Tags like `<strong>`, `<em>`, and `<blockquote>` mean something. Use them for their purpose, not just to change how text looks.

6. **Test With Sample Data** — Always verify your SQL queries and Python code with a few test entries. It catches mistakes early.

7. **Inline `style` Is Quick, External CSS Is Better** — For learning, inline styles are fine. For real projects, use separate CSS files.

8. **Images Need `alt` Text** — Always include alternative text. It helps accessibility, SEO, and users when images fail to load.

9. **Comments Explain Why, Not What** — Your code shows *what* it does. Comments explain *why* you did it that way.

10. **Build Projects to Learn** — Don't just read code. Type it out at least once. Better: modify it and predict the output first.

---

## 🏋️ Practice Tasks

### Easy Tasks (Great for Beginners)

**Task 1: Python Data Type Explorer**
- Create a variable for each data type: `int`, `float`, `str`, `bool`
- Print the type of each
- Try to add one number and one string—What error do you get?

**Task 2: Simple Type Conversion**
- Ask the user for two numbers using `input()`
- Convert both to integers
- Add them and print the result
- Example: Input "5" and "10" → Output "15"

**Task 3: Extend the HTML Page**
- Add a paragraph about what you want to study
- Use at least three different text formatting tags: `<strong>`, `<em>`, `<mark>`
- Add inline `style` to center and color your new paragraph

**Task 4: SQL Table Exploration**
- Create a new table called `students` with columns: name, age, grade
- Insert 3 students
- Select all rows
- Select only students where age > 20

---

### Medium Tasks (Moderate Challenge)

**Task 5: Age Calculator Program**
- Ask the user for their birth year
- Calculate their age (current year - birth year)
- Handle edge cases: What if they enter text instead of a number?

**Task 6: SQL Filtering Practice**
- Add 5 more characters to the `characters` table
- Write queries to find:
  - All characters older than 25
  - All characters in the "Straw hat" crew (watch your spelling!)
  - All characters WITHOUT a crew (use `IS NULL`)

**Task 7: HTML Profile Enhancement**
- Create a simple profile page with headings, paragraphs, lists, and images
- Use at least 5 different text formatting tags
- Use inline styles for colors and alignment
- Add an image from the web with a `title` attribute

---

### Hard Tasks (Challenge Yourself)

**Task 8: Python Input Validation**
- Ask the user for their age
- Repeat the question if they enter something that's not a number
- Only proceed when they give a valid number
- *Hint: Use a loop and `try/except`*

**Task 9: SQL Query Combinations**
- Create a `movies` table with columns: title, release_year, rating, genre
- Insert 10 movies
- Write complex queries:
  - Movies released after 2020 with rating > 8
  - Count how many movies exist in each genre
  - Find the oldest and newest movies

**Task 10: Multi-Language Integration**
- Create an HTML form (doesn't need to work yet, just the structure)
- Create a Python script that accepts user input for: name, email, age
- Plan how you'd store this data in SQL
- Document the types you'd use for each field and why

---

## ❓ FAQ

### Q1: What's the Difference Between `=` and `==`?

**In SQL**: `=` compares values (WHERE name = 'Luffy')  
**In Python**: `=` assigns values (age = 20), but `==` compares them (if age == 20)

**Example**

```python
age = 20        # Assignment: put 20 into age
if age == 20:   # Comparison: check if age holds 20
    print("You are 20")
```

### Q2: Why Does `int("5.5")` Crash?

Because `int()` expects a whole number. It doesn't know how to handle the decimal point.

**Solutions**

```python
float("5.5")      # 5.5 ✓ This works
int(float("5.5")) # 5 ✓ Convert to float first, then int
int(5.5)          # 5 ✓ Direct conversion of a numeric variable
```

### Q3: When Should I Use `NULL` vs `""`?

**NULL** → The data is unknown or missing  
**Empty string** → The data exists but is blank

**Example**

```sql
-- NULL: We don't know the crew
INSERT INTO characters (name, age, crew_name) VALUES ('UnknownShip', 50, NULL);

-- Empty string: There is no crew (by choice)
INSERT INTO characters (name, age, crew_name) VALUES ('Rogue', 35, '');
```

### Q4: Why Use `IS NULL` Instead of `= NULL`?

Because `NULL` is special in SQL. It represents "unknown," so `NULL = NULL` doesn't return true—it returns unknown. To check for NULL, use `IS NULL`.

### Q5: Can I Store a Picture Directly in SQL?

Technically yes (using `BLOB` type), but it's not recommended. Instead:
1. Save the image file on a server
2. Store the file path or URL in SQL
3. Load and display the image using the URL

This is more efficient and flexible.

### Q6: What's the Difference Between `float` and `DECIMAL` in SQL?

- **FLOAT** → Approximate decimal numbers, faster, less precise
- **DECIMAL(10,2)** → Exact decimal numbers, perfect for money, slower

**Use DECIMAL for money. Always.**

```sql
price DECIMAL(10,2)  -- Correct: exactly two decimal places
salary FLOAT         -- Less precise: might be 50000.0000001
```

### Q7: How Do I Update or Delete Data in SQL?

This comes in Day 03, but preview:

```sql
UPDATE characters SET age = 20 WHERE name = 'Luffy';
DELETE FROM characters WHERE crew_name IS NULL;
```

### Q8: What If My `input()` Causes a Crash?

Wrap it in `try/except`:

```python
try:
    age = int(input("Enter your age: "))
except ValueError:
    print("Please enter a number, not text!")
```

### Q9: How Do I Format Text in HTML Without Semantics?

Use `<span>` (inline) or `<div>` (block) with `style`:

```html
<span style="color: red; font-weight: bold;">Red bold text</span>
```

But prefer semantic tags for meaning: `<strong>` for importance, `<em>` for emphasis.

### Q10: Is Inline CSS Styling Bad?

For learning: No, it's fine.  
For large projects: Yes. Use separate CSS files.

**Reason**: Inline styles can't be reused, making code repetitive and hard to maintain.

---

## 📝 Summary

**Day 02 teaches the single most important concept in programming: data types matter.**

You learned how Python, SQL, and HTML all have their own way of classifying information. You discovered that `"5"` is not the same as `5`. You practiced converting data between types. You built a database table and queried it. And you formatted HTML to display information beautifully.

If you can explain these three ideas to a friend, you've mastered Day 02:

1. Every programming language has data types. Choose the right one for your data.
2. Converting between types is sometimes necessary—and you must do it deliberately.
3. Use `input()`, convert immediately, store it, use it: three steps, always.

You're now ready for Day 03, where you'll learn to modify data (UPDATE, DELETE) and write more complex queries. **Keep going. Be consistent.**

---

**Last Updated**: April 10, 2026  
**Status**: Complete & Ready to Learn  
**Next Step**: Review each practice file, run the code, modify it, and predict the output before running it again.

Keep practicing daily. Small steps every day build strong full-stack skills.
## Next Day

Continue to [Day 03](../Day_03/README.md).
