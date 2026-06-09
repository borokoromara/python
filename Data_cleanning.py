text= "  Engineering".lstrip()
print(text) # "Engineering"

text = "Engineering  ".rstrip()
print(text) # "Engineering"


text = "  Engineering  ".strip()
print(text) # "Engineering"


#Attention: Only removes spaces at the start or ends, not in the middle
text = "  Data Engineering  ".strip()
print(text) # "Data Engineering"

#And thoses methods will not will not only remove the white spaces , it could remove any characters you want from the start and end – not just spaces
text = "xxxyyyData Engineeringxxxyyy".strip("xy")
print(text) # "Data Engineering"

"""Use Case – Detect Extra Spaces
Check the length before and after strip () to find unwanted spaces
"""
text = "  Data Engineering  "
print(len(text)) # 22

#print the length of the same value, so text but this time after applying a strip methods
print(len(text.strip())) # 16


#Now we can do very nice stuff like this. We say the length of the original data minus the length of the my data but after cleaning up.
text = "  Data Engineering  "
extra_spaces = len(text) - len(text.strip())
print(extra_spaces) # 6

"""Data Cleansing
Case Conversion
"""

text = "Data Engineering"
print(text.upper()) # "DATA ENGINEERING"
text = "Data Engineering"
print(text.lower()) # "data engineering"


"""Use Case – Clean Data for Matching
Lowercase all text to prevent case-based mismatches during search or comparison
"""
text1 = "Data Engineering"
text2 = "data engineering"  
print(text1 == text2) # False

# Convert both to lowercase for comparison
print(text1.lower() == text2.lower()) # True

"""Best practice – Clean Before Search
Always trim spaces and lowercase your data and search term before matching

"""
search_term = "data engineering"
data = "  Data Engineering  "
search_term = search_term.strip().lower()
data = data.strip().lower()
print(search_term == data) # True


"""We have messy string a single clean summary with name, role and age : "968-Maria,  (D@t@ Engineer  );;  27y  "
I want to clean this up and make it more organized in one string. So here we have a name, role and age.
"""
messy_string = "968-Maria,  (D@t@ Engineer  );;  27y  "
# Step 1: Remove unwanted characters
cleaned_string = messy_string.strip()
# Step 2: Replace remaining unwanted characters
cleaned_string = cleaned_string.replace("@", "a")
# Step 3: Split the cleaned string into components
name, role, age = cleaned_string.split(",")
# Step 4: Clean up each component
name = name.strip().split("-")[1]  # Extract name after the hyphen
role = role.strip().strip("()")  # Remove parentheses
age = age.strip().strip("y")  # Remove 'y' from age
# Step 5: Format the cleaned components into a summary string
summary = f"Name: {name}, Role: {role}, Age: {age}"
print(summary) # Name: Maria, Role: Data Engineer, Age: 27

"""String Functions
Searching
"""

#Search
phone = "+33-123-456-7890"
# Is the phone code France? Check the country code (+33)
print(phone.startswith("+34")) # False
print(phone.startswith("+33")) # True

email  = "maria@example.com"
# Is the email from gmail? Check the domain (gmail.com)
print(email.endswith("gmail.com")) # False
print(email.endswith("example.com")) # True


file = "data_engineering_report.csv"
# Is the file a CSV? Check the extension (.csv)
print(file.endswith(".csv")) # True


"""Another example:
Is this a valid email address? check for (@)"""
email = "   maria@example.com   "
print("@" in email) # True
print(email.count("@") == 1) # True


"""Another example
Check if the URL is an API endpoint
"""
url = "https://api.example.com/v1/data"
print(url.startswith("https://api.")) # True or
print("/api." in url) # True

#Something that find is always combined with some other task. Find() is great when combined with other methods to add dynamics 
phone1 =  "+33-324-4456-232"
phone2 = "87-654-45"
phone3="0048-546-12654"
#Extract only phone number without country code 
print(phone1[4:])
print(phone2[3:])
print(phone3[5:])

# use find()
print(phone1.find("-")) # 3
print(phone2.find("-")) # 2
print(phone3.find("-")) # 4


# we want to start from the next character from the position number four
print(phone1[phone1.find("-") + 1:]) # 33-324-4456-232
print(phone2[phone2.find("-") + 1:]) # 87-654-45
print(phone3[phone3.find("-") + 1:]) # 48-546-12654


"""String Functions
Validating
    """

# Validation
# Check if the country name conatains only letters
country = "France"
print(country.isalpha()) # True
country = "United States1"
print(country.isalpha()) # False


"""We have another method, this time we’re going to check whether the string value has only numbers. 
So it contains only digit. It has no characters or any special characters"""
postal_code = "75001"
print(postal_code.isdigit()) # True or
print(postal_code.isnumeric()) # True

# add special characters to the postal code
postal_code = "75001-1234"
print(postal_code.isdigit()) # False


