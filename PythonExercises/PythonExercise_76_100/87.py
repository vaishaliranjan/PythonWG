with open(r"C:\Users\vranjan\Downloads\countries_missing.txt", "r") as file:
    content = file.readlines()

checklist = ["Portugal", "Germany", "Spain"]
checklist=[check+"\n" for check in checklist]
content= sorted(checklist+content)

with open(r"C:\Users\vranjan\Downloads\countries_missing.txt", "w") as file:
    file.seek(0)
    for c in content:
        file.write(c)
    file.truncate()

