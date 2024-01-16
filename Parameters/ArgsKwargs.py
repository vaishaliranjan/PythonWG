def add_all(a1,a2,a3,a4):
    return a1+a2+a3+a4

print(add_all(1,2,3,4))
tup= (1,2,3,4)
print(add_all(*tup))


def add_all_numbers(*args):
    return sum(args)


print(add_all_numbers(1,2,3,4))
#print(add_all_numbers("vaishali","ranjan"))

print(add_all_numbers(*tup))


def pretty_print(**kwargs):
    for k,v in kwargs.items():
        print(f"For {k} we have {v}.")

pretty_print(username="vaishali", password="vaishali")
pretty_print(**{'username':"vaishali", 'password':"vaishali"})