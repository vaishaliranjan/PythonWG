user_input=input("Write comma separated input: ")
content = user_input.split(",")
with open("commaseparated.txt", "w") as file:
    for c in content:
        file.write(c+'\n')