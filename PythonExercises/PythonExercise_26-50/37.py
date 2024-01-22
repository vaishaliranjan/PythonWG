path=r"C:\Users\vranjan\Downloads\words2.txt"
with open(path,"r") as file:
    content= file.read()
    content= content.replace(","," ")
    word_count= content.split()
    print(len(word_count))
