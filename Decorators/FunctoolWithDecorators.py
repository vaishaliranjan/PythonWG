user={
    "username":"vaishali",
    "access_level":"admin"
}
import functools
def user_has_permission(func):
    @functools.wraps(func)
    def secure_func():
        if user.get("access_level")=="admin":
            return func()

    return secure_func


@user_has_permission
def my_function():
    """
    this is my function
    :return:
    """
    return "The password is Admin1234"


@user_has_permission
def somehting():
    """
    this is something function
    :return:
    """
    pass


print(my_function())
print(somehting())
print(my_function.__name__)
print(somehting.__name__)

print(my_function.__doc__)
print(somehting.__doc__)
