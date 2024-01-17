class Dog:

    number_of_legs= 4
    __private_datatype=100
    _protected_datatype=199
    def __init__(self, name):
        self.name =name
        print("Base cons called")

    @classmethod
    def class_method(cls,data1):
        print(cls.number_of_legs)
        print(data1)
        print(cls.__name__)

    @staticmethod
    def static_method(data2):
        print(data2)

class Labrador(Dog):
    def __init__(self,name):
        print("Derived cons called")
        super().__init__(name)
    #pass

labrador1= Labrador("baby")
print(labrador1.name)
labrador1.class_method("DATA 1")
# labrador1.class_method("Data 1 printed")
# labrador1.static_method("Data 2 printed")
# print(labrador1.number_of_legs)
#
# labrador1.number_of_legs=10
# print(labrador1.number_of_legs)
# print(Dog.number_of_legs)
# Dog.number_of_legs=100
# print(labrador1.number_of_legs)
# print(Dog.number_of_legs)
#
# print(labrador1._protected_datatype)




# Multiple inheritance
class Class1:
    def __init__(self):
        pass
    def func1(self):
        print("func1 from class 1")

class Class2:
    def __init__(self):
        pass
    def func1(self):
        print("func1 from class 2")

class Class3(Class2,Class1):
    def __init__(self):
        Class1.__init__()



c3 = Class3()
c3.func1()


