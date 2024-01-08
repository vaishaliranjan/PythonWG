def hundred_numbers():
    i=1
    while i<100:
        yield i
        i=i+1

print([x*2 for x in hundred_numbers()])
g=hundred_numbers()
print(g)
print(next(g))
print(next(g))

my_range= range(10)
print(my_range.__repr__())