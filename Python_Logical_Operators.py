# Logical operations
print(3 > 1 and 5 < 1)  # False
print(3 > 1 and 5 > 1)  # True

print(3 > 1 or 5 < 1)   # True
print(3 > 1 or 5 > 1)     # True

# checks if the system is under pressure

cpu_usage = 70
memory_usage = 80
print(cpu_usage > 75 or memory_usage > 75)  # True


# Checking user credentials before login
email = True
password = False
print(email and password)  # False


email = True
password = True
print(email and password)  # True

# NOT operator

print(not(- 3 >2))  # False
print(not(- 3 < 2))  # True

print(not False)  # True
print(not not True)   # False


name = ""
print(not name)  # True, because an empty string is considered False
print(not 0)     # True, because 0 is considered False
is_raining = False
print(not is_raining)  # True, because is_raining is False



"""Execution order
Parentheses () First """

#task: 
# Allow access only if the user is logged in
# or they are a guest
# but they must not be banned

is_logged_in = True
is_guest = False
is_banned = False
print((is_logged_in or is_guest) and not is_banned)  # we will get True

# but
is_logged_in = True
is_guest = False
is_banned = True
print((is_logged_in or is_guest) and not is_banned)  # we will get False
# nb: True vs False --> Ture

"""Python 
Challenges"""

#1.	Check if a user’s name is not empty and the age is greater than or equal to 18
name = "Saran"
age = 3
print(name and age >= 18)  # True

# 2. Check if the password is at least 8 characters long and does not contain spaces
password = "Abdg12345"
print(len(password) >= 8 and " " not in password)  # True

# 3.	Check if a user’s email is not empty, contains '@' , and ends with '.com'
email = "saran@example.com"
print(email and "@" in email and email.endswith(".com"))  # True

# 4. Check if a username is a string, is not None, and is longer than 5 characters
username = "saran123"
print(isinstance(username, str) and username is not None and len(username) > 5)  # True

# 5.	Check if the user is either an admin or an moderator, and either they’re not banned or they’ve verified their email
is_admin = False
is_moderator = True
is_banned = False
has_verified_email = True
print((is_admin or is_moderator) and (not is_banned or has_verified_email))  # True
