import requests
from bs4 import BeautifulSoup

page = requests.get("https://github.com/vaishaliranjan/PythonWG")
soup= BeautifulSoup(page.content, "html.parser")

h1_tags=soup.find_all("h1")

for content in h1_tags:
    print(content.string)