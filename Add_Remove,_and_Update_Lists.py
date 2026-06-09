
letters = ['a', 'b', 'c', 'd', 'e']
print("Original list:", letters)
# task: add the letter 'f' to the end of the list
letters.append('f')
print("List after adding 'f':", letters)

# task: add 'x' at the start of the list
letters.insert(0, 'x')
print("List after adding 'x' at the start:", letters)

# task: add 'y' between 'b' and 'c'
letters.insert(3, 'y')
print("List after adding 'y' between 'b' and 'c':", letters)



#And of course we don’t have to g=forgot about our 2D matrix.
matrix = [
         ['a','b','c'], # row 0
         ['d','e','f'], # row 1
         ['g','h','i']  # row 2
    ]     

# task: add new row o the end of matrix
new_row = ['x', 'y', 'x']
matrix.append(new_row)
print("Matrix after adding new row:", matrix)

# task: add new at the start of matrix
new_row_at_start = ['p', 'q', 'r']
matrix.insert(0, new_row_at_start)
print("Matrix after adding new row at the start:", matrix)

"""But now let’s go to something little bit more complex. 
Let’s say that I would like to extend the row #1 list with a new member. 
I would like to add at the end an X."""

matrix[1].append('x')
print("Matrix after adding 'x' to row 1:", matrix)

# task : add 'z' at the start of the list row # 0
matrix[0].insert(0, 'z')
print("Matrix after adding 'z' at the start of row 0:", matrix)


"""Change your list
Remove Items
"""
letters = ['a', 'b', 'c']
# task: remove everything from the list
letters.clear()
print("List after removing all items:", letters)


letters = ['a', 'b', 'a']
#task : Remove 'a' from the list
letters.remove('a')
print("List after removing 'a':", letters)


# removing by position
letters = ['a', 'b', 'c']

# the pop() method
# task: remove the last item from the list
last_item = letters.pop()


# task: remove the first item from the list
first_item = letters.pop(0)
print("First item removed:", first_item)
print("List after removing first item:", letters)

# matrix example

matrix = [
         ['a','b','c'], # row 0
         ['d','e','f'], # row 1
         ['g','h','i']  # row 2
    ]     

# remove the all items from row # 1
matrix.remove(['a','b','c'])
print("Matrix after removing row # 0:", matrix)

# task remove the last list
matrix.pop()
print("Matrix after removing the last list:", matrix)


#Task : remove 'e' from the matrix
matrix[0].remove('e')
print("Matrix after removing 'e':", matrix)


# task: remove the first item from the last list
matrix[-1].pop(0)
print("Matrix after removing the first item from the last list:", matrix)

# task: remove the last item from the first list
matrix[0].pop()
print("Matrix after removing the last item from the first list:", matrix)

# Update
letters = ['a', 'b', 'c']
# atsk: Update the first item of the first list to 'x'
letters[0] = 'x'
print("List after updating the first item to 'x':", letters)

# task: Update the last item of the value to 'y'
letters[-1] = 'y'
print("List after updating the last item to 'y':", letters)


# task: Update the content of the last list
matrix = [
         ['a','b','c'], # row 0
         ['d','e','f'], # row 1
         ['g','h','i']  # row 2
    ]
matrix[-1] = ['x', 'y', 'z']
print("Matrix after updating the last list:", matrix)



# task: update the first item of the first row
matrix[0][0] = '-'
print("Matrix after updating the first item of the first row:", matrix)


#task: # update the 'e' by '-'
matrix[1][1] = '-'
print("Matrix after updating 'e' to '-':", matrix)

# task: update the last value in the last list to '-'
matrix[-1][-1] = '-'
print("Matrix after updating the last value in the last list to '-':", matrix)



