# Analyis & checking of lists in python

# what is the highest value in the list?
numbers = [1, 2, 3, 4] 
print("Max:", max(numbers)) # 4
# what is the lowest value in the list?
print("Min:", min(numbers)) # 1
# what is the sum of all the values in the list?
print("Sum:", sum(numbers)) # 10
# the length of the list?
print("Length:", len(numbers)) # 4 this function works for anhy data type not just numbers but also strings and other data types as well.


# the all and any functions
# all() function returns True if all elements of the iterable are true (or if the iterable is empty).
# any() function returns True if any element of the iterable is true. If the iterable is empty, return False.

print("All:", all(numbers)) # True because all numbers are non-zero
print("Any:", any(numbers)) # True because at least one number is non-zero

# but if we have a zero in the list then all will be false but any will still be true
numbers = [0, 1, 2, 3]
print("All:", all(numbers)) # False because of the zero
print("Any:", any(numbers)) # True because at least one number is non-zero
# for the string value
print("All:", all(['a','', 'c'])) # True because all characters are non-empty
print("Any:", any(['a','', 'c'])) # True because at least one character is non-empty
print("All:", all(['', '', ''])) # False because all characters are empty(considered to missing values )


# Any
print("All:", all(numbers)) # True because the iterable is empty
print("Any:", any([1,0,2])) # True because at least one element is true


# count
# how many  times numers five appears in the list
numbers = [1, 2, 3, 4, 5, 5, 5]
print("Count of 5:", numbers.count(5)) # we will get 3


#Method Index.
# what is the index of the first occurrence of the number 5 in the list?
print("Index of 5:", numbers.index(5)) # we will get 4 because the first occurrence of 5 is at index 4 (0-based indexing)



# operator in

# check if the number 3 is in the list
print("Is 3 in the list?", 3 in numbers) # True because 3 is in the list
# check if the number 10 is in the list
print("Is 10 in the list?", 10 in numbers) # False because 10 is not in the list

# another example with strings
list1 = [1, 2, 3, 'hello', 'world']
list2 = [1, 2, 3, 'hello', 'world']
# check if those two lists are equal
print("Are the lists equal?", list1 == list2) # True because both lists have the same elements in the same order


# the opposite of that is not equal
list1 = [1, 2, 3, 'hello', 'world']
list2 = [1, 2, 3, 'hello', 'world', 4]
print("Are the lists not equal?", list1==list2) # False because the second list has an extra element (4)


#Comparison:
#The first list element are compared, if they’re equal, python moves to the next element
list1 = [1, 2, 3]
list2 = [1, 2, 4]   
print("Is list1 less than list2?", list1 < list2) # True because the first two elements are equal, but the third element (3) is less than the third element of list2 (4)
print("Is list1 greater than list2?", list1 > list2) # False because the first two elements are equal, but the third element (3) is less than the third element of list2 (4)


# but if you is operator,
list1 = [1, 2, 3]
list2 = [1, 2, 3]  
print("Is list1 the same object as list2?", list1 is list2) # False because list1 and list2 are different objects in memory, even though they have the same content


# the same thing with equality operator
list1 = [1, 2, 3]
list2 = [1, 2, 3] 
print(list1 == list2) # True because the equality operator checks for value equality, and both lists have the same content



