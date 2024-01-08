# cars = ["ok", "ok","faulty","ok"]
# for car in cars:
#     if(car=="faulty"):
#         print("This car is faulty, stopping..")
#         break
#     print("This car is "+car)
#
# for car in cars:
#     if (car == "faulty"):
#         print("This car is faulty, skipping..")
#         continue
#     print("This car is " + car)
with open("questions.txt","r") as file:
    for line in file.readlines():
        print
