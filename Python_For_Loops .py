# not smart
"""print("round; 1")
print("round; 2")
print("round; 3")
print("round; 4")
print("round; 5")"""

# smart

for i in (1,2,3,4,5):
   print(f"Round: {i}")

 # Use the same word
 # Variable --> singular 
 # Sequence --> pluriel 
 
items = (1,2,3,4,5)
for item in items:
   print(f"Round: {item}")


# list:
items = [1,2,3,4,5, "hello"]
for item in items:
   print(f"Round: {item}")

#NB: in the for loop that the items must be either be numbers or string values. You can go and do like a mix.

# exemaple:

items = "Python"
for item in items:
   print(f"Round: {item}")
   

# range:

for item in range(5):
    print(f"Round: {item}")

# specify the start and the end arguments

for item in range(1,5):
   print(f"Round: {item}")


#We use for loops to go through values and aggregate data like summing, counting or averaging

"""scores = [80, 50, 60, 75]
total = 0

for score in scores:
   total += scores
   print("Current Total:", total)
print("Final Total:", total)"""

# we will get an error

scores = [80, 50, 60, 75]
total = 0

for score in scores:
   total += score
   print("Current Total:", total)
print("Final Total:", total)

#To the next one . as we learned we can do data cleanup , data preparations using for loop.

files = [' Report.scv ',' DATA.csv ',' final.TXT '] #

""" and let’s go and add some evil white spaces on lefts on rights in order to have some bad quality. Here we have two issues. We have the leading and trailing spaces and well you can see we have sometimes lowercase and uppercase.
Now I’m data Engineer or Analyst and I would like to go and clean up the data before I do something about it. So here I have to do two things. 
-	First removing the spaces
-	Second making everything either lowercase or uppercase. 
So depends on the rule that I follow in my project. I have to change the cases. So in order to do that we would go and create a for loop.
"""

"""for file in files:
    file = file.strip().lower()
    print(f"Processing {file}")"""

"""Everything is lower and everything is following our rule.  I will like to go and get rid the TXT. 
Actually, we only allow CSVs.  So in order to do that we will add another transformation : replace"""


for file in files:
    file = file.strip().lower().replace('.txt','.csv')
    print(f"Processing {file}")


"""Break
Statement"""

names = ['Saran','Christiane','','Sayon']
for name in names:
   print(f"Name={name}")

   # we will get
   #Name=Saran
   #Name=Christiane
   #Name=
   #Name=Sayon

"""Now as you can see we have all the four value and the empty one even. Now let’s say that if there 
something empty in my data I don’t want to continue. I want to break the loop and to stop the program. 
So in order to do that we have to make a check."""

names = ['Saran','Christiane','','Sayon']
for name in names:
   if name == '':
      print('Empty value detected !')
      break
   print(f"Name={name}")


   """Continue
       Statement """
   
   names = ['Saran','Christiane','','Sayon']
for name in names:
   if name == '':
      print('Empty value detected !')
      continue
   print(f"Name={name}")
   

"""Pass
    Statement """

names = ['Saran','Christiane','','Sayon']
for name in names:
   if name == '':
      print('Empty value detected !')
      pass #todo: Handle Empty Value
      name = name.replace('','unknown')
   print(f"Name={name}")
   

