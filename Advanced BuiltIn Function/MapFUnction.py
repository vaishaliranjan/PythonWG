friends=["Shakuntala", "Rolf","Rajiv","Vaishali","Ritika"]
friends_lower = map(lambda friend: friend.lower(), friends)
print(friends_lower)


friends_lower_1=[f.lower()  for f in friends]
print(friends_lower_1)

friends_lower_1=(f.lower()  for f in friends)
print(friends_lower_1)