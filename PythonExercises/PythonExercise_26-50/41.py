import string
with open("alphabets.txt", "w") as file:
    for letter in string.ascii_letters:
        file.write(letter+"\n")