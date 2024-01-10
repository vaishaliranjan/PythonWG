# Int, float, string and tuples are immutable
#True and False -two addresses everyone points on that two location only
my_var = 10
print(id(my_var))
my_var +=1 #returns new object
print(id(my_var))
is_true= False
print(id(is_true))
is_true=True
print(id(is_true))
is_here= True
is_not_here= False

print(id(is_here))
print(id(is_not_here))

#dictionary, lists and sets are mutable

student={
    "name":"Vaishali",
    "age":20
}
print(id(student))
student["age"]=21 #change the same object
print(id(student))

