# import string
# with open("alphabets_in_two.txt","w") as file:
#     number=0
#     for letter in string.ascii_lowercase:
#         file.write(letter)
#         number +=1
#         if number%2==0:
#             file.write("\n")

import string
with open("alphabets_in_two.txt", "w") as file:
    number=0
    for letter1,letter2 in zip(string.ascii_lowercase[0::2],string.ascii_lowercase[1::2]):
        file.write(letter1+letter2+"\n")
