"""items = [1, 3, 5 , 7]
for item in items:
    print(item)
else:
    print("Loop in completed") """



"""The break statement really work hand in hand with the else statements and they look exactly the if else statements"""
# Check for even number

items = [1, 3, 4 , 7]
for item in items:
    if item % 2 == 0:
        print("Even Nr. Found", item)
        break
else:
    print("ALL numbers are odd")


#Check for Missing names in a List

names = ['MARA','CAMARA', 'LY','BALDE']
for name in names:
    if name is None:
        print("Found a missing name")
        break
else:
    print("All names are available")



#Task: Check if all Files are csv files

files = ['data.csv','product.csv','sale.pdf']

for file in files:
    if not file.endswith('.csv'):
        print(f"{file} is not a csv")
        break
else:
    print("All files are csv")


    """Challenges :
Check whether any filename appears more than once and find out whether we have duplicates or not.
Print " Duplicate found "if a duplicate exists, otherwise print "All files are unique".
    """

file_list = [
    'report.csv',
    'data.xlsx',
    'summary.docx',
    'report.csv',
    'data.csv'
]

seen = []

for file in file_list:
    if file in seen:
        print("Duplicate Found")
        break
    seen.append(file)
else:
    print("All files are unique")