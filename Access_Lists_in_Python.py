# Access & read
list = ['', 'a', 'b', 'c', 'd', 'e'] # list of letters
print(list) # print the whole list
print(list[0]) # access the first element
print(list[1]) # access the second element
print(list[2]) # access the third element



# Access and read

Matrix = [
    ['a','b','c'], # row 0
    ['c','d','e'], # row 1
    ['f','g','i']  # row 2

]

#task: get the whole Matrix
print(Matrix)

# task: get the last row of the Matrix
print(Matrix[2]) # or 
print(Matrix[-1])


#now let’s say that I don’t need the whole row I just we need one thing like for example. For example, I would like to get the h.
print(Matrix[2][2]) # get the element at row 2, column 2
# or
print(Matrix[-1][-1]) # get the last element of the last row


# task : get the first item of the first row
print(Matrix[0][0]) # get the element at row 0, column 0


# task : get the lletter e
print(Matrix[1][2]) # get the element at row 1, column 2


#Task: get the first two items from the list
list= ['a', 'b', 'c', 'd', 'e']
print(list[:2]) # get the first two elements of the list


#Task: get the last two items from the list
print(list[-2:]) # get the last two elements of the list
# or
print(list[3:5]) # get the elements from index 3 to index 4 (inclusive)

# get the wole list
print(list[:]) # get the whole list

# Access and read

Matrix = [
    ['a','b','c'], # row 0
    ['c','d','e'], # row 1
    ['f','g','i']  # row 2

]
# task:  get the first two rows (lists) from a list
print(Matrix[:2]) # get the first two rows of the matrix

# task:  get the last two rows (lists) from a list
print(Matrix[-2:]) # get the last two rows of the matrix
# or
print(Matrix[1:3]) # get the rows from index 1 to index 2 (inclusive)
# or
print(Matrix[1:]) # get the rows from index 1 to the end of the matrix


#we are slicing the rows. But how about to slice actually inside one specific row ? for example. I would like to get the G and H from the row number two.
print(Matrix[2][:2]) # get the elements from index 1 to index 2 (inclusive) of row 2

