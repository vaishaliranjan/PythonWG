class A:
    def __init__(self, x):
        self.x=x

    @property
    def get_value(self):
        return self.x

    @get_value.setter
    def set_value(self,value):
        self.x=value

a=A(4)
print(a.get_value)
a.set_value=10
print(a.get_value)


