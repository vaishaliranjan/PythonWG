file = open("User_data.txt","a+")
while True:
    user_input = input("Write a value: ")
    if(user_input)=="CLOSE":
        file.close()
        break
    else:
        file.write(user_input+"\n")


