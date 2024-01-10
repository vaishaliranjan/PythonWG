import re

email="vaihslai@gmail.com"
exp="[a-z\.]+"
matches= re.findall(exp,email)
#print(matches)

price = "Price: $18,345.50"
expression= 'Price: \$([0-9,]*\.[0-9]*)'

matches = re.search(expression, price)
print(matches[0]) # matches entire
print (matches[1]) #first thing in bracket


