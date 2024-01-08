# my_file = open("data.txt", "r")
# my_file_content= my_file.readline()
# my_file.close()
# print(my_file_content)

# user_input= input("Eter your name: ")
# my_file_write = open("data.txt","w")
# my_file_write.write(user_input)
# my_file_write.close()

friends = input("enter three friends names separated by commas no spaces pls: ").split(",")
people= open("data.txt", "r")
people_nearby= [line.strip() for line in people.readlines()]
people.close()

friends_nearby= set(friends).intersection((set(people_nearby)))
nearby_friends_file = open("nearby_friends.txt", "w")
for friend in friends_nearby:
    nearby_friends_file.write(friend+"\n")
nearby_friends_file.close()
