# class User:
#     def __init__(self, username, password):
#         self.username=username
#         self.password=password
#
#     def login(self):
#         return f"Logged in!"
#
#     def __repr__(self):
#         return f"<User {self.username}>"
#
# #
# # u1=User("vaishali","password")
# # print(u1)
#
# class Admin(User):
#     def __init__(self,username,password,access):
#         super().__init__(username,password)
#         self.access=access
#
#     def __repr__(self):
#         return f"<Admin {self.username} and Access: {self.access}>"
#
#     def to_dict(self):
#         return{
#             'username': self.username,
#             'password':self.password,
#             'access':self.access
#         }


class A:

    def method1(self):
        print('its in class A')


class B:

    def method1(self):
        print('its in class B')

    def method2(self):
        print("This is method 2 in class B")
        self.method1() # name can be changed to method 3

class C(B,A):
    def method1(self):
        print('its in class C') # name can be changed to method 3

c=C()
c.method2()


