#Task: build a counter from 1 to 5

"""count = 1
while count <= 5:
    print(count)
    count += 1"""

    # count +=2
count = 1
while count <= 5:
    print(count)
    count += 2

#Task: Write a program that keeps asking "Do you agree ?"   until the user types "yes"

answer = ""
while answer != "yes":
    answer = input("Do you agree ?(yes/no):")
print("Thank You")


# unstoppable loop.

"""while True:
    print("I'm unstoppable !") """ #ne pas lancer


"""while True:
     answer = input("Do you agree ?(yes/no):")
     if answer =="yes":
         break
     print("Thank You")"""


# use case:
#3 attempts
# yes within three attempts -->"Glad we're on the same page"
# Otherwise " 3 strikes. You're out !"

attempts = 0
while attempts < 3:
    answer = input("Do you agree ?(yes/no):")
    if answer == "yes":
        print("Glad we're on the same page")
        break
    attempts += 1
else:
    print("3 strikes. You're out")



