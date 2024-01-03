for num in range(3):
    print(num)

print("Second type of range")
for num in range(1,3):
    print(num)

for num in range(1,10,2):
    print(num)

#For loop on iterables
friends=["Vaihsali", "SHakuntala"]
for friend in friends:
    print(friend)

family=[
    {"Name":"Vaishali", "Age": 20},
    {"Name":"Shakuntala", "Age": 40}
]
for member in family:
    print(member)
    name= member["Name"]
    age= member["Age"]
    print(f"Your name is {name} and your age is {age}")