class FirstHundredGenerator:
    #This is iterator not iterable-> we can get next value using next
    def __init__(self):
        self.number=0

    def __next__(self):
        if self.number<100:
            current = self.number
            self.number+=1
            return self.number
        else:
            raise StopIteration()

    def __iter__(self):
        return self

g= FirstHundredGenerator()
print(g)
print(next(g))
print(g.__next__())

my_gen= FirstHundredGenerator()
#this is not possible
for i in my_gen:
    print(i)


