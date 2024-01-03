# def calculate_mpg(car):
#     mpg= car["mileage"]/car["fuel_consumed"]
#     name = f"{car['name']} with {car['model_number']}"
#     print(f"{name} gives {mpg}")

cars = [
    {"name":"Toyota", "model_number":"VXI", "mileage":4000, "fuel_consumed": 500},
    {"name":"Suzuki", "model_number":"VXI", "mileage":4800, "fuel_consumed": 500}
]

def calculate_mpg(car):
    mpg= car["mileage"] / car["fuel_consumed"]
    return mpg

def car_name(car):
    name = f"{car['name']} with {car['model_number']}"
    return name
def car_info(car):
    mpg= calculate_mpg(car)
    name = car_name(car)
    return f"{name} gives {mpg}"

for car in cars:
    print(car_info(car))

def divide(x,y):
    if(y==0):
        return "Undefined"
    return x/y

print(divide(3,0))
print(divide(10,2))