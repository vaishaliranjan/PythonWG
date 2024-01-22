def number_of_words(string):
    return len(string)

def number_of_words2(string):
    str2= string.split(" ") # divides based on the parameter given
    return len(str2)

print(number_of_words("Vaishali"))
print(number_of_words2("Vaishali Ranjan"))