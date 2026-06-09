#match
"""password = "123a670987"
print(len(password))

if len(password) < 8:
    print("Password must be at least 8 characters long")
else:    print("Password is valid")"""

# Use case -Word frequency Check
"""Counts how many times a specific word appears in a given text."""

text = """Pyhton is easy to learn.
Python is a popular programming language.
Many developers use Python for web development, data analysis, and machine learning."""

text.count("Python")
print(text.count("Python"))

""" Python is case sensitive, means uppercase and lowercase letters are treated as different characters."""

# Use case - Detect Suality Issues
"""Counts how many unwanted characters in my data."""
print(text.count("$"))