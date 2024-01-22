name="Vaishali"
greeting =f"Hello, {name}"

print(greeting)
#now even if we will change the value of the name it will still print the name defined above the f string variable as it is an interpretor
name="Bob"
print(greeting)

#now to make it dynamically we can print it using f string

username ="Shakuntala"
print(f"My name is {username}")

username ="Vaishali"
print(f"My name is {username}")