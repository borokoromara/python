"""score = 90
if score >=90:
    print("A")
else:
    print("F")"""


"""We're going and convert this to one in line"""
score =70
"A" if score >= 90 else "F"
# and put it in print()
print("A" if score >= 90 else "F")

# put it in a variable

grade = "A" if score >= 90 else "F"
print(grade)


# # Another more complex example where this time we have an else if
"""score = 90
if score >=90:
    print("A")
elif score >=80:
    print("B")
else:
    print("F")"""

grade = "A" if score >= 90 else "B" if score >= 80 else "F"
print(grade)



"""Special Statements
Match Case

Evaluate a value against multiple values runs the code of the first match."""

#--task: convert the full country names into 2-letter abbreviations

country = "United States"
if country == "United States":
    print("US")
elif country =="Guinea":
    print("GN")
elif country =="IRAN":
    print("IN")
elif country =="Germany":
    print("DE")
else:
    print("Unknown Country")

"""so can imagine how long this code go to be, so in Python and as well in any other programming 
language if you have this scenario where you have a value and you comparing it to multiple other 
options using the equal operators you can use the match case. The syntax or that is very simple"""

match country:
    case "United States":
        print("US")
    case "Guinea":
        print("GN")
    case "Iran":
        print("IN")
    case "Germny":
        print("DE")
    case _:
        print("Unknown Country")

#if you have like multiple variants that has the same output , you can separate that using the pipe

match country:
    case "United States" | "USA":
        print("US")
    case "Guinea":
        print("GN")
    case "Iran":
        print("IN")
    case "Germny":
        print("DE")
    case _:
        print("Unknown Country")