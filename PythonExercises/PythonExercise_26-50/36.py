path=r"C:\Users\vranjan\Downloads\words1.txt"
with open(path,"r") as file:
    content= file.read()
    word_count= content.split()
    print(len(word_count))
