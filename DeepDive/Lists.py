import sys

list1= ["Vaihsali","Ritika", "Ayush", "Akshat" ]
print(list1[0])
print(list1[-1])
#list slicing
print(list1[0:3])


#empty list
list2= list()
print(len(list2))

l1=list((0, 1, 2, 3, 4, 5, 6, 7, 8, 9))
print(l1)

l2=list({"circle", "square", "triangle", "rectangle", "pentagon"})
print(l2)

l3= list({"name": "John", "age": 30, "city": "New York"})
print(l3)
print(l3[0].__class__)

l4=list("Pythonista")
print(l4)

l5= list({"name": "John", "age": 30, "city": "New York"}.values())
print(l5)
print(l3[0].__class__)

l6= list({"name": "John", "age": 30, "city": "New York"}.items())
print(l6)
print(l6[0].__class__)

#append vs extend vs insert
list3= list()
list3.append((1,2))
print(list3[0])
# it takes only one argument
# list3.append(1,2)
# print(list3[1])

list3.extend({3,4,5})
print(list3[1])
print(list3)
print(list3[2].__class__)
print(list3[0].__class__)
#print(list3[10]) #Index Error

list3.insert(10,"Vaishali") # when inserting at higher number of index it appends it in the last
print(list3)

list3.insert(2,("AKSHAT", "AYUSH")) # when inserting at higher number of index it appends it in the last
print(list3)

list3.remove(("AKSHAT","AYUSH"))
print(list3) # removes first occurence and value error if not found

element=list3.pop()
print(element)
print(list3)
element=list3.pop(0)
print(list3)



# reverse
list3.reverse()
print(list3)
print(list3[::-1]) # no change in real
print(list3)
# sort

list3.sort()
print(list3)

# Nested
l11=[
    [1,2],
    [3,4]
]
print(l11)
print(len(l11))
print(l11[1][0])

# tuple inside list
l12=[
    (1,2),
    (3,4)
]
print(l12)
print(l11[1][0])

#set inside list
l13=[
    {1,2},
    {3,4}
]
print(l13)
print(l13[0])

#dictionary inside list
l14=[
    {
        "Name":"Vaishali",
        "Profile": "intern"
    },
    {
        "Name":"Ritika",
        "Profile": "intern"
    }
]
print(l14)
print(l14[0])
print(l14[0]["Name"])







