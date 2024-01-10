from bs4 import BeautifulSoup
SIMPLE_HTML = '''<html>
<head></head>
<body>
<h1>This is a title</h1>
<p class="subtitle">Lorem ipsum dolor sit amet. Consectetur edipiscim elit.</p>
<p>Here's another p without a class</p>
<ul>
    <li>Rolf</li>
    <li>Charlie</li>
    <li>Jen</li>
    <li>Jose</li>
</ul>
</body>
</html>'''

simple_soup = BeautifulSoup(SIMPLE_HTML,"html.parser")

print(simple_soup.find("h1"))

list_itms = simple_soup.find_all("li")
list_content=[e.string for e in list_itms]
print(list_content)
def find_title():
    h1_tag = simple_soup.find("h1")
    return h1_tag.string

print(find_title())



def find_subtitle():
    paragraph = simple_soup.find('p',{"class":"subtitle"})
    print(paragraph.string)

find_subtitle()

# def find_other_paragraph():
#     paragraphs = simple_soup.find_all('p')
#     other_paragraphs=[p for p in paragraphs if 'subtitle' not in p.attrs.get("class",[])]
#     print(other_paragraphs[0].string)
#
# find_other_paragraph()