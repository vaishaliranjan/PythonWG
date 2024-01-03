############################# LIST COMPREHENSION ###########

# numbers =[1,2,3,4,5]
# multiple_of_two= [number*2 for number in numbers]
# print(multiple_of_two)
#
# names =["Vaishali","Shakuntala","Shantanu", "Ritika"]
# names_lower = [name.lower() for name in names]
# print(names_lower)
# title_cased = [ name.title() for name in names_lower]
# print(title_cased)
#
# five = [5 for n in range(0,5)]
# print(five)

friends =["Vreeti", "Vaishali", "Asmi", "Ritika"]
guests=["VaiShali", "vreeti" ]
#
# lst = [friend.title() for friend in friends if friend.lower() in (g.lower() for g in guests)]
# print(lst)
#
# friends_lower = set([f.lower() for f in friends])
# guests_lower = set([f.lower() for f in guests])
# print(friends_lower.intersection((guests_lower)))

################################ SET COMPREHENSION #####################
# friends_lower= {f.lower() for f in friends}
# guests_lower= {g.lower() for g in guests}
# present_friends = {f.title() for f in friends_lower.intersection((guests_lower))}
# print(present_friends)

################################## DICTIONARY COMPREHENSION ################
# friends =["vaishali", "riitika"]
# age= [20,21]
# name_age= {
#     friends[i]:age[i] for i in range(len(friends))
# }
# print(name_age)
#
# name_age= {
#     friends[i]:age[i] for i in range(len(friends))
#     if age[i]>20
# }
# print(name_age)

############################ ZIP FUNCTION #######################
#Combine two lists
# friends =["vaishali", "riitika"]
# age= [20,21]
# numbers=[1,2]
# friends_age= dict(zip(friends, age))
# print(friends_age)
#
# friends_age= list(zip(friends, age)) # tuples inside list
# print(friends_age)
#
# friends_age= list(zip(friends, age, numbers)) # tuples inside lists
# print(friends_age)

############################### ENUMERATE FUNCTION ###########################
friends =["vaishali", "riitika"]
counter =0
for friend in friends:
    print(counter)
    print(friend)
    counter= counter+1

for counter, friend in enumerate(friends):
    print(counter)
    print(friend)

for counter, friend in enumerate(friends, start=1):
    print(counter)
    print(friend)

dictionary = dict(enumerate(friends))
print(dictionary)

lst=[(1,2),(3,4)]
dictt= dict(lst)
print(dictt)