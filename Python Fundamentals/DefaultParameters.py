#not allowed
#def add(x=3, y): -> agar aage hai toh peeche sbke pas hone chahiye


def add(x, y=3): #these are default params
    return x+y

print(add(2,5))
print(add(2))
print(add(y=4,x=10))
print(add(x=11))
print(add(3,y=10)) # these are named arguments
#not allowed
#print(add(x=10,3)) -> agar aage hai toh peeche sabke pas hone chahiye

print(1,2,3,4, sep="-")

default_y=10
def multiply(x, y=default_y): # stores the default value too so cant change and its a bad practice
    print(f"multiplication: {x*y}")

x= multiply(3)  #x would have value None as the function by default returns none
default_y=11
multiply(3)

