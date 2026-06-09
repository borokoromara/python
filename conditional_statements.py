#Standalone if :

score = 100
if score >= 90:
    print("A")
    print("grezat Job !")

"""in java :
if (socre >= 90 ){
    System.out.println("A")
    System.out.println("Great Job !");
    }"""

"""Two-way Decision
   If- else
"""

score = 95
if score >= 90:
    print("A")
else:
    print("F")


"""Multiple condition
if-elif-else"""

score = 85
if score >= 90:
    print("A")
elif score >=80:
    print("B")
else:
    print("F")

"""Breanching
if-elif-elif-else"""

score = 70
if score >= 90:
    print("A")
elif score >=80:
    print("B")
elif score >=70:
    print("C")
elif score >=60:
    print("D")
else:
    print("F")

    """So now back to our code let’s go and create a new variable submitted 
    project and assign it the value true."""


score = 90
submitted_project = True
if score >= 90:
    if submitted_project:
        print("A+")
    else:
        print("A")
elif score >=80:
    print("B")
elif score >=70:
    print("C")
elif score >=60:
    print("D")
else:
    print("F")

    """Connecting Conditions
Logical Operators 
"""

score = 100
submitted_project = False
if score >= 90 and submitted_project:   
    print("A+")
elif score >=90 and not submitted_project:
    print("A")
elif score >=80:
    print("B")
elif score >=70:
    print("C")
elif score >=60:
    print("D")
else:
    print("F")


"""Independent 
if - else """

score = 50
submitted_project = False

if score >= 90:
    print("High Score")
else:
    print("Low Score")

if submitted_project:
    print("project is sumitted")
else:
     print("project is not sumitted")


"""
#1: Validate the quality and correctness of email values
-	Must not be empty
-	Must contain '.' And '@'
-	Must contain exactly one '@' symbol
-	Must end with '.com', '.org', or '.net'
-	Must not be longer than 254 characters
-	Must start and end with a letter or digit
"""

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



#2 Python challenge
"""Validate the quality and correctness of passewords
- Must not be empty
- Must be at least 8 characters
- Must include at least 1 uppercase
- Must include at least 1 lowercase
- Must not be same as the email
- Must not conatin any spaces
- Must start and with a letter or digit"""


password = "eertyuoA"
email = ""

# Must not be empty
if password == "":
    print("Password must not be empty")

# Must be at least 8 characters
elif len(password) < 8:
    print("Password must be at least 8 characters")

# Must include at least 1 uppercase
elif not any(char.isupper() for char in password):
    print("Password must include at least 1 uppercase")

# Must include at least 1 lowercase
elif not any(char.islower() for char in password):
    print("Password must include at least 1 lowercase")

# Must not be same as the email
elif password == email:
    print("Password must not be the same as the email")

# Must not contain spaces
elif " " in password:
    print("Password must not contain spaces")

# Must start and end with a letter or digit
elif not (password[0].isalnum() and password[-1].isalnum()):
    print("Password must start and end with a letter or digit")

else:
    print("Password is valid")