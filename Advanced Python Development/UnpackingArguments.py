accounts={
    "savings":1000,
    "checking":213
}

def add_balance(amount, name):
    accounts[name] +=amount
    return accounts[name]

transactions=[
    (122,"checking"),
    (33,"savings")
]
transactions_dict=[{
    122:"checking",
    33:"savings"
}, {
    122:"checking",
    33:"savings"
}]

for t in transactions:
    add_balance(*t) # unpack list or tuples into arguments
    print(accounts["savings"])
    print(accounts["checking"])

class User:
    def __init__(self, amt, account):
        self.amt= amt
        self.account = account

user_objects =[User(**t) for t in transactions_dict]
print(user_objects)


