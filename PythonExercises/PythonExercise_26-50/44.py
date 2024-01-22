# import string
# with open("alphabets_in_two.txt","w") as file:
#     number=0
#     for letter in string.ascii_lowercase:
#         file.write(letter)
#         number +=1
#         if number%2==0:
#             file.write("\n")

import string
with open("alphabets_in_three.txt", "w") as file:
    number=0
    for letter1,letter2,letter3 in zip(string.ascii_lowercase[0::3],string.ascii_lowercase[1::3],string.ascii_lowercase[2::3]):
        file.write(letter1+letter2+letter3+"\n")
