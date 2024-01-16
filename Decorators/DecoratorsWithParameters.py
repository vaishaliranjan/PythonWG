user={
    "username":"vaishali",
    "access_level":"admin"
}
import functools

def third_level(access_level):
    def user_has_permission(func):
        @functools.wraps(func)
        def secure_func(panel):
            if user.get("access_level")==access_level:
                return func(panel)

        return secure_func
    return user_has_permission


@third_level("admin")
def my_function(panel):
    """
    this is my function
    :return:
    """
    return f"The {panel} password is Admin1234"





print(my_function("movies"))

#but this is limited
