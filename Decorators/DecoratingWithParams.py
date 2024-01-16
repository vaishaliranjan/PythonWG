user={
    "username":"vaishali",
    "access_level":"admin"
}
import functools
def user_has_permission(func):
    @functools.wraps(func)
    def secure_func(panel):
        if user.get("access_level")=="admin":
            return func(panel)

    return secure_func


@user_has_permission
def my_function(panel):
    """
    this is my function
    :return:
    """
    return f"The {panel} password is Admin1234"





print(my_function("movies"))

#but this is limited
