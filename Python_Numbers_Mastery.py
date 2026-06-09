x = "24"
Y = 5.7
z = 2 + 3j
print(type(x))
print(type(Y))
print(type(z))

print(x * 3)

x = int(x)
print(type(x))

print(x * 3)

# conbersion

a = 3.14
print(int(a))
print(float(a))

"""Numbers
Math Operators
"""

print (2 + 3)   # Addition
print (5 - 2)  # Subtraction
print (4 * 3)  # Multiplication
print (10 / 2) # Division
print (10 // 3) # Floor Division
print (2 ** 3) # Exponentiation
print (10 % 3) # Modulus


x = 2
X = x + 3
x += 3
print(X)

x -= 2
print(x)
x *= 4
print(x)


"""Numbers Functions
Rounding
"""

# Measure Distance
distance = 5.6789
# Round to 2 decimal places
rounded_distance = round(distance, 2)
print(rounded_distance)

#Useful for measuring distances, or size , regardless of direction 
print(2 - 1) # -8
print(abs(2-8 )) # 8



# rounding Numbers
price = 19.9955876
rounded_price = round(price, 2)
print(rounded_price)


# Rounding Numbers
price = 19.5955876
rounded_price = round(price, 2)
print(rounded_price)

"""floor() is not a built-in function,
floor() belongs to the math module - import it before using """

#print(floor(rounded_price)) 
"""as you can sse there is like something wrong with the code because we have not imported the math module yet
"""
# this function exists somewhere in the standard library. But first you have to  import math.
import math
print(math.floor(rounded_price))
print(math.ceil(rounded_price)  )
print(math.trunc(rounded_price))    
print(int(rounded_price))


# int() vs trunc()
#if you're not using math already, just use int() it's simple and built -in
# if you've already imported math, unse truc() it makes your intent cleaner.

# round(): Handy in data nalyisi to clean up numbers for reports or save space
# ceil() : Perfect for data engineering -like splitting data into pages or batches


"""Number Functions
Random
"""

import random
print(random.random())
print(random.randint(1, 10)) # inclusive of both 1 and 10
# Use it to generate test data (dummy) for like age, ID, or prices

"""Number Functions
Validation
"""
#is_integer(): checks if a float no decimal part(is a whole number)

x = 7.0
print(x.is_integer()) # True because 7.0 has no decimal part

x = 7.1
print(x.is_integer()) # False because 7.1 has a decimal part


# isinstance(value,type) built-in function: checks if a value belongs to a certain data type

x =70
print(isinstance(x, int)) # True because x is an integer
print(isinstance(x, float)) # False because x is not a float


# Python Challenge
# Generate a random integer between 1 and 100 and check if the result is an even number

random_number = random.randint(1, 100)
print(random_number)
if random_number % 2 == 0:
    print(f"{random_number} is an even number.")
else:
    print(f"{random_number} is an odd number.")
     