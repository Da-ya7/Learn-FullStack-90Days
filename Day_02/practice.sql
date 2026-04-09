-- Day 02 — SQL Practice
-- Topic: Data types: INT, VARCHAR, DATE, BOOLEAN, TEXT, DECIMAL. CREATE TABLE students (id INT, name VARCHAR(50), age INT);

-- Write your queries below:
/*Just like Python, SQL columns also have types. When you create a table, you must tell SQL what kind of data each column holds.*/
--Data types in SQL
-- int - wholenumbers - ex:age,id,etc..
--VARCHAR(n) - Text up to n characters - ex:name VARCHAR(50)
--TEXT - Long text, no limit - description, bio
--DECIMAL(p,s) - Precise decimals - price DECIMAL(10,2)
--DATE	A date: - YYYY-MM-DD - 2025-01-15
--BOOLEAN - True (1) or False (0) - is_active

/*Create your first table
A table is like a spreadsheet. You define the columns and their types. Then you fill it with rows.*/

USE onepiece_db;

CREATE TABLE characters(
    name varchar(50),
    age int,
    crew_name text
);

--This creates an empty table with 3 columns. Now let's add some rows:

INSERT INTO characters (name,age,crew_name)
VALUES ('luffy',19,'Straw_hat');

INSERT INTO characters (name,age,crew_name)
VALUES ('Z0r0',22,'Straw hat');

INSERT INTO characters (name,age,crew_name)
VALUES ('Sanji',22,'Straw hat');

--SELECT is the most important SQL command. It reads data from a table. You'll use this in literally every SQL query you ever write.

SELECT * from characters;--to select all rows and columns

SELECT name,crew_name from characters; --to select specific column

SELECT * FROM characters WHERE age > 20; -- Get only rows that match a condition (WHERE)

SELECT * FROM students WHERE name = 'Luffy'; --Get a specific person

/*reading SELECT statements
Read SQL like English: SELECT name, age FROM students WHERE age > 20 = "Give me the name and age FROM the students table WHERE age is greater than 20."*/

/*NULL vs empty string
This is a concept beginners often miss. NULL means "no value at all — the data is missing". An empty string "" means "the value exists, but it's blank".*/

-- Insert a row where crew_name is missing (NULL)
INSERT INTO students (name, age, crew_name)
VALUES ('Garp',72,NULL);


-- Find rows where city is missing
SELECT * FROM characters WHERE crew_name IS NULL;

-- Note: WHERE crew_name = NULL does NOT work — always use IS NULL