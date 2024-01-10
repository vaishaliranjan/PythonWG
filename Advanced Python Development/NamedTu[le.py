from collections import namedtuple
account =("checking", 1345.09)
print(account[0])
print(account[1])

Account = namedtuple('Account',['name','balance'])
account = Account('Checking',balance= 1235.3)
print(account)
print(account.name)