class Student:
    def __init__(self, name, school):
        self.name= name
        self.school= school
        self.marks=[]

    def avg(self):
        return sum(self.marks)/len(self.marks)

class WorkingStudent(Student):
    def __init__(self,name,school,salary):
        super().__init__(name,school)
        self.salary= salary

    @property
    def weekly_salary(self):
        return self.salary*37.5

rolf= WorkingStudent("Vaishali","GHSS",24500)
print(rolf.salary)
#print(rolf.weekly_salary())

#use no arg method as property- @property- this is a decorator
print((rolf.weekly_salary))