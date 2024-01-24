while True:
    user_input= input("ENter a password: ")

    if any( i.isdigit() for i in user_input) and any( i.isupper() for i in user_input) and len(user_input)>=5:
        print("password is okay")
        break
    else:
        print("password is not okay")