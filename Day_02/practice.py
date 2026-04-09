# Day 02 — Python Practice
# Topic: Data types: int, float, str, bool, type(). Type conversion: int(), str(), float(). Input() from user.

# Write your code below:

#data types
age = 20 #int=whole number ex: -2,55
price = 99.99 #float number with decimal point
name = "Dhayalan" #both text and number wrapped in quotes ex:Agent007
is_active=True

print(type(age))
print(type(price))
print(type(name))
print(type(is_active))

#-------------------------------------------------------------------------------------------------------------------------------------
"""Sometimes you need to convert one type to another. For example, when a user types their age, Python receives it as text (str), not a number. You need to convert it."""
#typeconversion
# str to int
age_str="20"
age_int=int(age_str)
print(type(age_str))
print(type(age_int))
print(age_int+5) #adding integer
print(age_str+ "5") #adding string

# int to str
score = 100
message = "Your score: " + str(score)
print(message)          # Your score: 100

# int to float
x = 5
print(float(x))          # 5.0

# float to int (drops the decimal)
y = 9.8
print(int(y))            # 9  (NOT rounded — decimal just cut off)

"""Common beginner mistake: "5" + 5 crashes in Python because you cannot add a string and a number. You must first convert: int("5") + 5 = 10."""

#--------------------------------------------------------------------------------------------------------------------------------------------
#Getting input from the user
"""The input() function lets users type something. Everything from input() comes back as a string — always convert it if you need a number."""
name=input("Enter your name:") #getting string as a input
print(f"hello {name}")

age =int(input("enter your age:"))
print(f"your age is {age}")

height = float(input("Enter your height in cm:"))
print(f"your height is {height}")

#----------------------------------------------------------------------------------------------------------------------------------------------
#Practice — build this
#Write a program that asks the user for their name and birth year, then calculates and prints their approximate age:

your_name=input("Enter your name:")

birth_year=int(input("Enter your birth year:"))
age=2025-birth_year
print(f"Your name is {name} and your approximate age is {age}")

#---------------------------------------------------------------------------------------------------------------------------------------------------------

"""End of Day1 python ...Be consistent one day you will become what you want"""