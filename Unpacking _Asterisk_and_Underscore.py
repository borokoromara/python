#Python Unpacking Asterisk * and Underscore _

person= ["John", 29 , 'Data Engineer', "France"]
name= person[0]
age= person[1] 
role= person[2]
country= person[3]


#Now we’re going to do the same thing , but this time we’re going to make a list of variable name
name, age, role, country = person
print(name)
print(age)
print(role)
print(country)


# now i'm interested with the first item and the last item. but verything in between is actually don't matter.

name, *details, country = person
print(name)
print(details)
print(country)

#Now what else we can do is that if you know what I’m interested only with the first item and everything else not interesting for me even the last item
name, *details= person
print(name)
print(details)

"""Of course exactly we can do the opposite where we say you know what the 
last item is the most important one and everything else the rest is actually not interesting even the first item."""
*details, country = person
print(details)
print(country)


#    Unpacking Rules
# RULE: Number of variables must match the values exactly- not less, not more

numbers = [1, 2, 3, 4]
first, second, third, last = numbers # ValueError: too many values to unpack (expected 3)


#But if now if you go and remove one of them with that we have three variables
numbers = [1, 2, 3, 4]
first, second, third = numbers # ValueError: too many values to unpack (expected 3)

#And the same thing if you have actually too many so third fourth wow if you execute
numbers = [1, 2, 3, 4]
first, second, third, fourth, last = numbers # ValueError: not enough values to unpack (expected 5, got 4)


#so the number of variable s must be exactly matching if you are not using asterisk.
numbers = [1, 2, 3, 4]
first, second, third, last = numbers
print(first)
print(second)  
print(third)
print(last)


#but now of course you could have here less variables if  you say

numbers = [1, 2, 3, 4]
first, *middle, last = numbers
print(first)
print(middle)
print(last)

#Now one more cool things. Let’s say that I have only one item. But actually I have two variables like this. So I have the 
numbers = [1]
first, *rest = numbers # ValueError: not enough values to unpack (expected 2, got 1)
print(first)
print(rest)

#If you have remeve asterisk then you must have two items otherwise you will get an error
numbers = [1]
first, rest = numbers # ValueError: not enough values to unpack (expected 2, got 1)
print(first)
print(rest)

#it works with anything that has a sequences.
numbers = 'Hi'
first, *rest = numbers
print(first)
print(rest) 



#Skippingg Items
#Underscore "_"


person= ["John", 29 , 'Data Engineer', "France"]
name, _, role, _ = person
print(name)
print(role)


"""Now the things is I really don’t care about all those in the middle. 
I will never use it. So it is totally waste of space if I do that. So now how we go to fix it ? 
if you go and use only the underscore, you have to add an underscore for each variable in the middle. """


person= ["John", 29 , 'Data Engineer', "France"]
name, *_, country = person
print(name)
print(country)