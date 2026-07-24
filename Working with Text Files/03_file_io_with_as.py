###############################################
#
# Using with ...... as ....... for opening file and doing the operations
#
# Using with ....... as ...... dont required for closing the file after doing the operations                 
#
###############################################

# Here we open the file, writing into the file and the file closes automatically

# IMPROVED: Changed "a+" to "r" since we are only reading the data. 
# If you must use "a+", remember to add file.seek(0) before file.read()!
with open("text.txt", "r") as file:
    data = file.read()
    print(data)
    
print("We dont need the close() function")
