###############################################
#
# Using with ...... as ....... for opening file and doing the operations
#
# Using with ....... as ...... dont required for closing the file after doing the operations                  
#
###############################################

# Here we open the file, writing into the file and the file closes automatically

with open("text.txt","a+") as file:
    data = file.read()
    print(data)
print("We dont close() function")
