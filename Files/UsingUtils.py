# import utils.file_operations
#
# print(utils.file_operations.read_file("csv_file.csv"))
# utils.file_operations.save_to_file("Ritika", "nearby_friends.txt")

from utils.file_operations import read_file,save_to_file

print(read_file("csv_file.csv"))
save_to_file("Ritika", "nearby_friends.txt")