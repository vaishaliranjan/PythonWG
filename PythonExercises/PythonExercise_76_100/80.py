# while True:
#     user_input= input("ENter a password: ")
#
#     if any( i.isdigit() for i in user_input):
#         if any( i.isupper() for i in user_input):
#             if len(user_input)>=5:
#                 print("password is okay")
#                 break
#             else:
#                 print('Minimum length required is 5')
#         else:
#             print("Need atleast one uppercase letter")
#     else:
#         print("Need atleast one digit")


while True:
    notes = []
    psw = input("Enter password: ")
    if not any(i.isdigit() for i in psw):
        notes.append("You need at least one number")
    if not any(i.isupper() for i in psw):
        notes.append("You need at least one uppercase letter")
    if len(psw) < 5:
        notes.append("You need at least 5 characters")
    if len(notes) == 0:
        print("Password is fine")
        break
    else:
        print("Please check the following: ")
        for note in notes:
            print(note)