import random
characters = "abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?"

choosen= random.sample(characters,6)
password= "".join(choosen)
print(password)