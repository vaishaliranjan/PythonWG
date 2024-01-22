# c = 1
# def foo():
#
#     return c
# foo()
# print(c)


def foo():
    global c
    c = 1
    return c
foo()
print(c)