class Car:
    def __init__(self):
        print("Object created")

class Garage:
    def __init__(self):
        self.cars=[]

    def __len__(self):
        return len(self.cars)

    def add_car(self, car):
        if not isinstance(car, Car):
            raise TypeError(f"try to add a car")
        #raise NotImplementedError("We cant add cars yet")
        #print("This method is work in progress")
        self.cars.append(car)


ford=Garage()
ford.add_car(Car())
try:
    ford.add_car("car")
except TypeError:
    print("This is not a car")
except ValueError:
    print("Something weird happened")
finally:
    print(f"The garage now has{len(ford)} cars")
