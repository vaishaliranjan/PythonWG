location = ["Yazali", "Shimla"]

def check_Y(location):
    return location.startswith("Y")

#locations = filter(check_Y,location)
locations =[l for l in location if l.startswith("Y")]
if any(locations):
    print("There is one ")

if all(locations):
    print('There is all')