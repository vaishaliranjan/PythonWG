def starts_with_r(friend):
    return friend.startswith('R')

friends=["Shakuntala", "Rolf","Rajiv","Vaishali","Ritika"]

#start_with_r= filter(starts_with_r,friends) # this is a generator
start_with_r= filter(lambda x:x.startswith("R"), friends)
print(start_with_r)
print(next(start_with_r))
print(next(start_with_r))
print(next(start_with_r))
# print(next(start_with_r))
# print(next(start_with_r))

another_starts_with_r= (f for f in friends if f.startswith("R"))
#Generator comprehensions are faster


def my_custom_filter(func,iter):
    for i in iter:
        if func(i):
            yield i