class Student:
    s_name="DHS"
    def __init__(self,name, age):
        self.name=name
        self.age=age

    @classmethod
    def func1(cls):
        cls.s_name="sfc"
        s_name="SSD"
        print(Student.s_name)
        print(cls.__name__)

    @staticmethod
    def func2():
        s_name="SDDDD"

s= Student("vas",23)
s1=Student("s",346)
print(Student.s_name)
Student.func1()
s.func1()
s.func2()
Student.func2()
s.s_name="scf"
print(Student.s_name)
print(s.s_name)
print(s1.s_name)