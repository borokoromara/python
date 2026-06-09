#Task: Loop through a list of days and print only the working days skipping the weekends

#1. Skip weekends in calendar loop

days = ['Mon','Sun','Wed','Tue']
weekends = ['Sat','Sun']
for day in days:
    if day in weekends:
        continue
    print(f"WorkDay: {day}")



#task2:  Scan emails to block unsafe data from entering your system
emails = [
    'data@gmail.com',
    'sanan@outlook.de',
    'DROP TABLES USERS;',
    'marai@gmail.com'
]

for email in emails:
    if ';' in email:
        print("SQL Injection: Hacker Attack")
        break
    print(f"Processing Email: {email}")