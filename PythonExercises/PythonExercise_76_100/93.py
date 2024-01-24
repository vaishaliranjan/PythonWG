import glob
file_list= glob.glob(r"C:\Users\vranjan\Downloads\subdirs\subdirs\**\*py", recursive=True)
print(len(file_list))