# name = input("Enter your name: ")
# username = "vaishali"
#
# if name ==username:
#     print("Welcome back!")
# else:
#     print("Helo stranger!")

friends = ["Vaishali", "Ritika", "Vreeti"]
family = ["Shakuntala", "Rajiv", "Shantanu"]
name = input("Enter your name: ")
if name in friends:
    print("Hello friend!")
elif name in family:
    print("Hello family!")
else:
    print("Hello stranger")