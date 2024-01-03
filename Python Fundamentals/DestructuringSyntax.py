number = 0.8, 1, 3 #a tuple
first, second, third= number
print(first)
print(second)
print(third)

# a list of tuples
friends= [("Vaishali", 20), ("Ritika", 21)]
for name, age in friends: # this will get to know that we have tupples inside the list
    print(name,age)
    #name= friend[0], age = friend[1]