import json

with open("csv_file.txt", "r") as file:
    lines = [line.strip().split(",") for line in file.readlines()]
    json_file = [{"club": line[0], "country": line[2], "city": line[1]} for line in lines]

json.dump(json_file, "json_file.txt")