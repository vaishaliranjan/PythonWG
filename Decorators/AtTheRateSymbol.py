user={
    "username":"vaishali",
    "access_level":"admin"
}

def user_has_permission(func):
    def secure_func():
        if user.get("access_level")=="admin":
            return func()

    return secure_func


@user_has_permission
def my_function():
    return "The password is Admin1234"


@user_has_permission
def somehting():
    pass
print(my_function())
print(somehting())
print(my_function.__name__)
print(somehting.__name__)
