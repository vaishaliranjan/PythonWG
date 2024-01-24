with open(r"C:\Users\vranjan\Downloads\urls.txt","r+") as file:
    urls = file.readlines()
    urls=[url.strip() for url in urls]
    file.seek(0)
    for url in urls:
        url=url.replace("s","",1)
        url=url[:6]+"/"+url[6:]
        print(url)
        file.write(url + "\n")
    file.truncate()




