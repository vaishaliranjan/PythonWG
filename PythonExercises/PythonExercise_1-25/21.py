d = {"a": 1, "b": 2, "c": 3}
d=dict((x,y) for x,y in d.items() if y<=1)
print(d)
#dictionary comprehension
# dict(then same as exp but (x,y) as in tuple)