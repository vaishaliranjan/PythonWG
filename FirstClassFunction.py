# avg = lambda sequence: sum(sequence)/ len(sequence)
# top = lambda sequence: max(sequence)
# total = lambda sequence: sum(sequence)

students=[
    {"name": "Vaishali","grades":[99,100]},
    {"name": "Ritika","grades":[99,100]}
]

operations={
    "average": lambda sequence: sum(sequence)/ len(sequence),
    "max": max,
    "sum": sum
}
for student in students:
    name= student["name"]
    grades= student["grades"]

    print(f"{name} ")
    operation = input('Enter the operation average, max, sum: ')
    operation_perform = operations[operation]
    print(operation_perform(grades))
# All functions in Python are just variables, which means you can pass them to other functions as arguments.