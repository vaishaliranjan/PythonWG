with open(r"C:\Users\vranjan\Downloads\countries_clean.txt", "r") as file:
    countries = file.readlines()
    countries= [line.strip() for line in countries]

checklist = ["Portugal", "Germany", "Munster", "Spain"]
checklist=[country for country in checklist if country in countries]
print(checklist)