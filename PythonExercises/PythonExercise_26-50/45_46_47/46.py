import string
alphabet_list=[]
for letter in string.ascii_lowercase:
    with open(letter+".txt","r") as file:
        alphabet_list.append(file.read())
print(alphabet_list)