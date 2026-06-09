# Create Lists

empty_list = [] # empty list
print(empty_list)
print(type(empty_list))

# there a multiple ways on how to put data inside a list

empty_list = [] # empty list
letters = ['a', 'b', 'c', 'd', 'e'] # list of letters
numbers = [1, 2, 3, 4, 5] # list of numbers
names = ['Alice', 'Bob', 'Charlie', 'David'] # list of names
mixed_list = [1, 'Alice', 3.14, True, None] # list with mixed data types
print(empty_list)
print(type(empty_list))
print(letters)
print(type(letters))
print(numbers)
print(type(numbers))
print(names)
print(type(names))
print(mixed_list)
print(type(mixed_list))


# Create Lists

empty_list = list() # empty list
print(empty_list)

# Now of course if you want to put item inside it, you have to use something inside the function.

letters = 'abcde' # list of letters
print(letters)


#so I don’t want to have it as s string value. It is very simple. 

letters = list('abcde') # list of letters
print(letters)

#. And of course, for the list function we can pass any data type that actually a sequence a sequence
numbers = list(range(6)) # list of numbers 6
print(numbers)


# Nested Lists
nested_list = [[1, 2, 3], ['a', 'b', 'c'], [True, False]] # list of lists
print(nested_list)