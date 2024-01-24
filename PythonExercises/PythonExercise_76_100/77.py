from datetime import datetime
age= int(input("ENter your age: "))
year= datetime.now().year - age
print(f"You were born back in {year}")