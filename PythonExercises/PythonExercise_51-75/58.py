import json
with open("data.json", "r+") as file:
    content = json.load(file)
    file.seek(0)
    content["employees"].append({'firstName': 'Vaishali', 'lastName': 'Ranjan'})
    json.dump(content,file)
    file.truncate()