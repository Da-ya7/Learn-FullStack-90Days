# Day 03 — Python Practice
# Topic: String methods: upper(), lower(), strip(), split(), replace(), find(), count(), startswith(). String length.

# ============================================
# 1. STRING LENGTH
# ============================================
text = "Hello, World!"
print(f"Length of '{text}': {len(text)}")

name = "Python"
print(f"Name length: {len(name)}")


# ============================================
# 2. upper() - Convert to uppercase
# ============================================
message = "welcome to python"
upper_message = message.upper()
print(f"Original: {message}")
print(f"Upper: {upper_message}")


# ============================================
# 3. lower() - Convert to lowercase
# ============================================
title = "HELLO WORLD"
lower_title = title.lower()
print(f"Original: {title}")
print(f"Lower: {lower_title}")


# ============================================
# 4. strip() - Remove leading/trailing whitespace
# ============================================
text_with_spaces = "   Python Programming   "
stripped = text_with_spaces.strip()
print(f"Original: '{text_with_spaces}'")
print(f"Stripped: '{stripped}'")

# Remove specific characters
text_special = "###Python###"
removed = text_special.strip("#")
print(f"Removed #: '{removed}'")


# ============================================
# 5. split() - Split string into list
# ============================================
sentence = "Python is awesome and powerful"
words = sentence.split()
print(f"Sentence: {sentence}")
print(f"Split by space: {words}")

csv_data = "apple,banana,orange,grape"
fruits = csv_data.split(",")
print(f"Split by comma: {fruits}")


# ============================================
# 6. replace() - Replace part of string
# ============================================
text = "I love JavaScript, JavaScript is great"
new_text = text.replace("JavaScript", "Python")
print(f"Original: {text}")
print(f"Replaced: {new_text}")

# Replace only first occurrence
limited_replace = text.replace("JavaScript", "Python", 1)
print(f"Replace first only: {limited_replace}")


# ============================================
# 7. find() - Find index of substring
# ============================================
sentence = "The quick brown fox jumps over the lazy dog"
index = sentence.find("brown")
print(f"Index of 'brown': {index}")

not_found = sentence.find("cat")
print(f"Index of 'cat': {not_found} (returns -1 if not found)")


# ============================================
# 8. count() - Count occurrences of substring
# ============================================
text = "banana is yellow, banana is sweet"
count_banana = text.count("banana")
print(f"Text: {text}")
print(f"Count of 'banana': {count_banana}")

count_a = text.count("a")
print(f"Count of 'a': {count_a}")


# ============================================
# 9. startswith() - Check if string starts with substring
# ============================================
headline = "Breaking News: Python 4.0 Released!"
if headline.startswith("Breaking"):
    print("It's breaking news!")

url = "https://google.com"
if url.startswith("https"):
    print("This is a secure connection")


# ============================================
# 10. PRACTICAL EXAMPLES - Combined Methods
# ============================================
print("\n=== PRACTICAL EXERCISES ===\n")

# Exercise 1: Email validation
email = "  JOHN.DOE@GMAIL.COM  "
cleaned_email = email.strip().lower()
if "@" in cleaned_email:
    print(f"Valid email format: {cleaned_email}")

# Exercise 2: Text processing
user_input = "  Hello World from Python  "
processed = user_input.strip().lower().replace("python", "programming")
print(f"Processed text: {processed}")

# Exercise 3: Parse comma-separated values
data = "John, 25, Engineer, NYC"
info = data.split(",")
name = info[0].strip()
age = info[1].strip()
print(f"Name: {name}, Age: {age}")

# Exercise 4: Check file type
filename = "document.pdf"
if filename.lower().endswith(".pdf"):
    print(f"File is a PDF: {filename}")

# Exercise 5: Word frequency
poem = "the quick brown fox jumps over the lazy dog"
word_list = poem.split()
print(f"Total words: {len(word_list)}")
print(f"Words starting with 'the': {poem.count('the')}")

