#Mutables are passed by ref actually-> change inside func will be highlighted across outside the function
#where as immutables are  actually passed by reference

#Immutable
num=10
def change_num(num):
    print(id(num))
    num= num+5
    print(id(num))

print(id(num))
change_num(num)
print(id(num))

#Mutable
dictt={
    "name":300,
    "see":33
}
def change_dict(dictt, key):
    dictt[key]=10
    print(id(dictt))

print(id(dictt))
change_dict(dictt,"name")
print(id(dictt))