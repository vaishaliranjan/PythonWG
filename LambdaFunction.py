# lambda functions are functions that takes input perorm some operation and returns output

average = lambda sequence: sum(sequence)/len(sequence)

students=[
    {"name": "Vaishali","grades":[99,100]},
    {"name": "Ritika","grades":[99,100]}
]

for student in students:
    print(average(student["grades"]))