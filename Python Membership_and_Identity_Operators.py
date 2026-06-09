print("o" in "Python")  # True
print("y" in "Python")  # True
print("z" in "Python")  # False
print("P" not in "Python")  # False
print("p" not in "Python")  # True


print( 3 in [1, 2, 3, 4, 5])  # True
print( 6 in [1, 2, 3, 4, 5])  # False
print( 6 not in [1, 2, 3, 4, 5])  # True
print( 3 not in [1, 2, 3, 4, 5])  # False

# security check : ensure teh domain is not banned

domain = "gmail.com"
banned_domains = ["baddomain.com", "spamdomain.com", "malicious.com"]
print(domain not in banned_domains)  # True, because "gmail.com" is not in the list of banned domains


domain = "malicious.com"
banned_domains = ["baddomain.com", "spamdomain.com", "malicious.com"]
print(domain not in banned_domains)  # False, because "malicious.com" is in the list of banned domains


"""Identity operators
Is – is not
"""
x = ['a', 'b', 'c']
y = ['a', 'b', 'c']

print(x == y)  # False, because x and y are different objects in memory
print(x is y)  # False, because x and y are different objects in memory


x = 10
y = 10
print(x == y)  # True, because x and y have the same value
print(x is y)  # True, because small integers are cached by Python and x and y refer to the same object in memory



# task : validate the email adddress it must be filled in and not empty
email = "b@gmail.com"
print(email != "")  # False, because email is an empty string
print(email)  # Output: (empty string)

# Nome-means no value at all, it is unknown  "" means an empty but it is known, it is string

email = None
print(email is not None and email != "")  # False, because email is an empty string
print(email) 

# Use is instead of == when checking for None
