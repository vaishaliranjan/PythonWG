class User:
    def __init__(self, name, metrics):
        self.name=name
        self.metrics=metrics

    def __repr__(self):
        return f"<User {self.name}>"

def email_engaged_user(my_user):
    try:
        print(calculate_operation(my_user))
    except KeyError:
        print("The values arent suitable")
        raise
    else:
        print("Only when error not occured")
    finally:
        print("This is finally block")

def calculate_operation(my_user):
    return my_user.metrics["key"]+my_user.metrics["value"]

my_user= User("Vaishali",{"key":10, "value":20})
email_engaged_user(my_user)
