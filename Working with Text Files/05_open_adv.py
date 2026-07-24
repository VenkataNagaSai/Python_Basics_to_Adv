###############################################
#
# Using with ...... as ....... for opening file and doing the operations
#
# Using with ....... as ...... dont required for closing the file after doing the operations                  
#
###############################################

# Here we open the file, writing into the file and the file closes automatically

###############################################
#
# Should we use a or r
#
############################################### 

with open("text.txt","a+") as file:

###############################################
#
# we use seek() to jump to the required line and when we use append the cursor jumps to end of the file but we need to read the file from begning
#
############################################### 

    pointer = file.tell()
    print(f"Cursor is located at : {pointer} before using the seek(0)\n")

    file.seek(0)

    pointer = file.tell()
    print(f"Cursor is located at : {pointer} after using seek(0) method\n")

###############################################
#
# we can use the same read() and print() method to read & print the data
# 
############################################### 

    data = file.read()

    print(data)

print("We dont close() if with ..... as ..... used because its automatically closed")
