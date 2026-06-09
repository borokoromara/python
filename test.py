email = "kabalo@gmail.com#"

# Clean the String
email = email.strip()  # enlève les espaces au début et à la fin

# Email must not be empty
if email == "":
    print("Email cannot be empty")

# Email must contain '.' and '@'
elif not ('.' in email and '@' in email):
    print("Email must contain . and @")

# Email must contain exactly one '@' symbol
elif email.count('@') != 1:
    print("Email must contain exactly one @.")

# Email Must end with '.com', '.org', or '.net'
elif not email.endswith(('.com', '.org', '.net')):
    print("Email must end with .com,, .org or .net")

# Email Must not be longer than 254 characters
elif len(email) > 254:
    print("Email not be longer than 254 characters")
# Email Must start and end with a letter or digit
elif not(email[0].isalnum() and email[-1].isalnum()):
    print("Email must start and end with a letter or digit")
else:
    print("Email is valid")


# remplace elif by if

email = "kabalo@gmail.com#"
valid= True
# Clean the String
email = email.strip()  # enlève les espaces au début et à la fin

# Email must not be empty
if email == "":
    print("Email cannot be empty")
    valid = False
# Email must contain '.' and '@'
if not ('.' in email and '@' in email):
    print("Email must contain . and @")
    valid = False
# Email must contain exactly one '@' symbol
if email.count('@') != 1:
    print("Email must contain exactly one @.")
    valid = False
# Email Must end with '.com', '.org', or '.net'
if not email.endswith(('.com', '.org', '.net')):
    print("Email must end with .com,, .org or .net")
    valid = False
# Email Must not be longer than 254 characters
if len(email) > 254:
    print("Email not be longer than 254 characters")
    valid = False
# Email Must start and end with a letter or digit
if not(email[0].isalnum() and email[-1].isalnum()):
    print("Email must start and end with a letter or digit")
    valid = False
if valid:
    print("Email is valid")

