# Comparison operators

print(100 == 100)  # True
print(100 == 200)  # False
print(100 != 200)  # True
print(100 > 50)   # True
print(100 < 50)   # False
print(100 >= 100) # True
print(100 <= 100) # True

# Strings Can be comparered too !
# you can compare strings too alpahbetically, not just numbers
print("Hello" == "Hello")  # True
print("Hello" == "hello")  # False  

# Python is case-sensitive
# So "a" and "A" are treated as different characters values
print("a" == "A")  # False
print("a" > "A")   # True, because lowercase letters have higher ASCII values


# Don't mix them up !
# = assigns, == compares
x = "a"  # This is an assignment, x is now "a"

print(1<4)  # True
print(1>4)  # False

# Chained comparison
# check multiple conitions in one line, just like in math
print(1 < 2 < 3)  # True
print(1 < 3 < 2)  # False


# chained comparisons works lile SQL's BETWEEN they check if a value is between two bounds
# example : Is age between 18 and 30 ?
age = 25
print(18 <= age <= 30)  # True
