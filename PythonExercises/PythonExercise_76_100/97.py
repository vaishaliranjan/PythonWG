file = open("User_data_Save.txt","a+")
list=[]
while True:
    user_input = input("Write a value: ")
    if(user_input)=="SAVE":
        file.close()
        file = open("User_data_Save.txt","a+")
    elif user_input=="CLOSE":
       file.close()
       break
    else:
        file.write(user_input+"\n")


