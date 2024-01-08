file = open("csv_file.csv","r")
lines = file.readlines()
file.close()
lines =[line.strip() for line in lines[1:]]

for line in lines:
    person_data= line.split(",")
    name = person_data[0].title()
    age=person_data[1]
    degree= person_data[2].capitalize()
    college= person_data[3].title()

    print(f"{name} with age {age} is studying {degree} at {college}")


sample_csv_value= ",".join(["Rolf","20","mit","jyappee"])
print(sample_csv_value)
