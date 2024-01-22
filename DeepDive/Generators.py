def get_number(n):
    for x in range(0,n+1):
        yield x

y= get_number(1)
print(y)
print(next(y))
print(next(y))
print(next(y))