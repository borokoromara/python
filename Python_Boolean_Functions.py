print(True)
print(False)
#type of boolean
print(type(True))
print(type(False))

# convert
print(bool(1225))
print(bool(0))
print(bool(""))
print(bool("Hello"))

# none isn't Empty - it's missing value
# None means no value. "" Empty means the value exists, but empty string
print(bool(None))


# functions any and all
email = ""
phone = "0176-12345678"
username = ""

# task: Allowq registration if any fiel is filled
print(any([email, phone, username]))

email = ""
phone = "0176-12345678"
username = "Saran2023"

#task2: allows registration only of all fieals are filled
print(all([email, phone, username]))


# istance function
# isisntance (value,type) built-in function : checks if a value belongs to a certain data type
print(isinstance(123, int))
print(isinstance(True, str))

# another example

"Hello".endswith("o") # returns True
"Hello".startswith("H") # returns True