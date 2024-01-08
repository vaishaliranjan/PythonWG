class MyCustomError(TypeError):
    '''
    This excepiton is raised when needed
    '''
    def __init__(self,message, code):
        super().__init__(f"Error code {code}: {message}")
        self.code= code


#raise MyCustomError("A new error ", 500)
err= MyCustomError("err", 400)
print(err.__doc__)