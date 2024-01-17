from abc import ABCMeta,abstractmethod

class Animal(metaclass=ABCMeta):
    def walk(self):
        print("Walking..")


    @abstractmethod
    def num_legs(self):
        pass

class Dog(Animal):
    def num_legs(self):
        print("4")

class Monkey(Animal):
    def num_legs(self):
        print("2")

#a=Animal()
d=Dog()
m=Monkey()

animals= [Dog(),Monkey()]
for a in animals:
    a.num_legs()
    print(isinstance(a,Animal))