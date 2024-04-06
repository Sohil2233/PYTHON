import random

# random integere between 1 and 10
c = random.randint(1,10)
print(c)

# /random float between 0 and 1
c = random.random()
print(c)

# heads or tails
c=random.randint(0,2)
if c==1:
  print("Heads")
else:
  print("Tails")

import my_module
print(my_module.pi)#it prints 3.14


# list 
cities_sangli=["sangli","bagni","ashta"]
# access item in list
print(cities_sangli[0])
print(cities_sangli[-1])
# to chage content in list
cities_sangli[1]="baagni"
# to add content in list
cities_sangli.append("korba")
print(cities_sangli[3])
# to extend list
cities_sangli.extend(["islampur","panus"])
print(cities_sangli)


dirty_dozen=["strawberries","spinach","kale","nectarines","apples","grapes","peaches"]
fruits=["strawberries","nectarines","apples","grapes","peaches"]
vegetables=["spinach","kale"]
dirty_dozen=[fruits,vegetables]
print(dirty_dozen)





















