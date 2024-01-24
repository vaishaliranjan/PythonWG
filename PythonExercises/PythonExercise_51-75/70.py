import requests

content= requests.get("https://pythonhow.com/media/data/universe.txt")
print(content.text)