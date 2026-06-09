for x in range(3): # outer loop
    for y in range(2): # inner loop
        for z in range(2):
              print(f"{x},{y},{z}")


"""
Nested Loop
Real-Worl Applications
"""
#The first use case is for crossing and combining our data or we call it pairing the data

colors = ['red','blue','green']
sizes = ['L','M','S']

#now let’s go say that I would like to go and generate maybe a product catalog with all 
#combinations of colors and sizes.  So I want to pair each color with each size. 
# In order to to that we can use the nested loops

for color in colors:
     for size in sizes:
          print(f"{color} - Size{size}")


#the second use case and the most important one. We use it in order to go through layers. Or we call it drilling into hierarchy. 

years = [2026, 2027]
months = ['jan','Feb']
days = range(1,29)

for y in years:
     for m in months :
          for d in days:
               print(f"report_{y}_{m}_{d}.csv")


#Task: SELECT count(*) FROM customers where id IS NULL;

tables = ['customers','orders','products','prices']
columns = ['id','create_date']
for t in tables:
     for c in columns:
          print(f"SELECT count(*) FROM {t} WHERE {c} IS NULL;")