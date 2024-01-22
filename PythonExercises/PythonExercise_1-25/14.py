# a = ["1", 1, "1", 2]
# b= set(a)
# print(b)
#
# from collections import OrderedDict
# a = ["1", 1, "1", 2]
# b=OrderedDict.fromkeys(a)
# print(b)


a = ["1", 1, "1", 2]
b=[]
for x in a:
    if x not in b:
        b.append(x)
print(b)