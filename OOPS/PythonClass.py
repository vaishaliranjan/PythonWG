# my_students ={
#     'name': "Vaishali Ranjan",
#     "grades": [20,100,80,99]
# }
#
# avg = lambda sequence: sum(sequence)/len(sequence)
#
# print(avg(my_students["grades"]))
#
# print(id(my_students))
#
# a=100
# b=100
# print(f"{id(a)} and {id(b)}")


##########################################CLASSSSS##########################
# class Student:
#     def __init__(self, new_name, grades):
#         self.name= new_name
#         self.grades= grades
#
#     def avg(self):
#         return sum(self.grades)/len(self.grades)
#
#
# student_one = Student("Vaishali", [100,99,100,99])
# student_two = Student("Shantanu",[91,99,10,77])
# print(student_one) #print address
# print(student_one.name)
# print(student_one.grades)
# print(student_one.__class__)
# print(id(student_one.grades[1]))
# print(id(student_two.grades[1]))
#
# print(student_one.avg())
# print(Student.avg(student_one))

class Garage:
    def __init__(self):
        self.cars=[]

    def __len__(self):
        return len(self.cars)

    def __getitem__(self, item):
        return self.cars[item]

    def __repr__(self):
        return f"<Garage {self.cars}>"

    # def __str__(self):
    #     return f"Garaeg with {len(self)} cars"

ford = Garage()
ford.cars.append("Toyota")
ford.cars.append("Suzuki")
print(len(ford))
print(ford[0])

# if we have defines len and getitem magic methods in our function then we can iterate over the object

for car in ford:
    print(car)

print(ford)