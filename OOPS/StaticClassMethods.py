class FixedFloat:
    def __init__(self, amount):
        self.amount= amount

    def instance_method(self):
        print("This is an instance method. We would need to create instance")

    @staticmethod
    def static_method():
        print("This is a static method")

class Euro(FixedFloat):
    def __init__(self, amount):
        super().__init__(amount)
        self.symbol = "$"

e1 = Euro(25000)
e1.static_method()
FixedFloat.static_method()
Euro.static_method()