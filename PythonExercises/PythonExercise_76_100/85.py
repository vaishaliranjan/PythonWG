with open(r"C:\Users\vranjan\Downloads\countries_raw (1).txt","r+") as file:
    content= file.readlines()
    content=[line.strip() for line in content]
    content=[line for line in content if line!=""]
    content=[line for line in content if line!="Top of Page"]
    content = [line for line in content if len(line)!=1]
    file.seek(0)
    for c in content:
        file.write(c+"\n")
    file.truncate()


