# sorting
letters = ['c', 'a', 'b']
# sort the list in ascending order
letters.sort()
print("Sorted list:", letters) # we will get ['a', 'b', 'c']

# sort the list in descending order
letters.sort(reverse=True)
print("Sorted list (descending):", letters) # we will get ['c', 'b', 'a']


matrix = [
         ['d','d','d'], # row 0
         ['g','h','i'], # row 1
         ['a','b','c']  # row 2
    ]

# sort the first row in ascending order
matrix.sort()
print("Matrix after sorting row 0:", matrix)


# sort the second row in ascending order
matrix[1].sort()
print("Matrix after sorting row 1:", matrix)

# sort the third row in ascending order
matrix[2].sort()
print("Matrix after sorting row 2:", matrix)


# sort the data in specific row #1
matrix[1].sort()
print("Matrix after sorting row #1:", matrix)


# task: sort the data without changing the original list
letters= ['c', 'a', 'b']
new_list = sorted(letters)
print("Original list:", letters) # we will get ['c', 'a', 'b
print("Sorted list:", new_list) # we will get ['a', 'b', 'c']

# task: reverse the order of items in the list
letters = ['a', 'b', 'c']
letters.reverse()
print("List after reversing:", letters) # we will get ['c', 'b', 'a']



"""And now here again we have the same scenario as the sort. We can do the reverse on an extra copy. 
So that we don’t change the original copy."""


# task: reverse the order of items in the list without changing the original list
letters = ['a', 'b', 'c']
new_list = list(reversed(letters))
print("Original list:", letters) # we will get ['a', 'b', 'c']
print("Reversed list:", new_list) # we will get ['c', 'b', 'a']
