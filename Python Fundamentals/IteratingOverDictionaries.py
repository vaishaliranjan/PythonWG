friend={"Vaishali":20,"Ritika": 21}
for name in friend:
    print(name) # this will print the keys only

for age in friend.values():
    print(age)#this will print the age

for item in friend.items():
    print(item) #both

for name, age in friend.items():
    print(f"Your name is {name} and age is {age}")