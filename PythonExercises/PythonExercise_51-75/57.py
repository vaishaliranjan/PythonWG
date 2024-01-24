import json
with open("data.json", "r") as file:
    content = json.load(file)
    print(content)