import json

file = open("friends.json","r")
file_content= json.load(file)
file.close()
print(file_content["friends"][0])

cars= [
    {"name": "Totota","Models":"VXI"},
    {"name":"Lamborghini", "Models":"RRXI"}
]

file=open("cars_json.txt","w")
json.dump(cars, file)
file.close()

my_json_string ='[{"Name":"Alpha","released":1950}]'
incorrect_car = json.loads(my_json_string)
print(incorrect_car[0]["Name"])
friend={
    "name":"vaishali"
}
message = json.dumps(friend)
print(message)
print(message.__class__)
#loads convert string to dictionary and dumps convert dictionary to string
#load -> reads a json file and converts it into dictionary
#dump-> convert dictionary to file