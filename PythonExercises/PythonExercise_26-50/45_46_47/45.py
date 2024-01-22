import string
for letter in string.ascii_lowercase:
    file= open(letter+".txt","w")
    file.write(letter)
    file.close()

for letter in string.ascii_lowercase:
    with open(letter+".txt", "w")  as file:
        file.write(letter)