# accounts={
#     "current":2888,
#     "savings":4444
# }
#
# def change_values(num: int, name:str = "current")-> int:
#     accounts[name]+=2
#
# change_values(2,"savings")
# print(accounts["savings"])
#
# change_values(2)
# print(accounts["current"])

# def add_balance(name: str, acc:str, account_balance:list =[]):
#     account_balance.append(acc) #this list is being generated at the time funtion
#     #is created so it will act as one list
#     print(id(account_balance))
#     print(account_balance)
#
# a1=add_balance("vasihai","savings")
# a2= add_balance("vsajb","sgb")

#either this or pass none
# def add_balance(name: str, acc:str, account_balance:list ):
#     account_balance.append(acc) #this list is being generated at the time funtion
#     #is created so it will act as one list
#     print(id(account_balance))
#     print(account_balance)
#
# a1=add_balance("vasihai","savings",[])
# a2= add_balance("vsajb","sgb",[])

def add_balance(name: str, acc:str, account_balance:list= None ):
    if not account_balance:
        account_balance=[]
    account_balance.append(acc) #this list is being generated at the time funtion
    #is created so it will act as one list
    print(id(account_balance))
    print(account_balance)

a1=add_balance("vasihai","savings",[])
a2= add_balance("vsajb","sgb",[])
