# iterable methods have iter dunder func

#generator with iter dunder fuction becomes iterable
class AnotherIterable:
    def __init__(self):
        self.cars=["fiesta","toyota"]

    def __len__(self):
        return len(self.cars)

    def __getitem__(self, item):
        return self.cars[item]

for car in AnotherIterable():
    print(car)

my_numbers =[x for x in [1,2,3,4,5]]
my_numbers_gen =(x for x in [1,2,3,4,5])

print(my_numbers_gen)
print(next(my_numbers_gen))