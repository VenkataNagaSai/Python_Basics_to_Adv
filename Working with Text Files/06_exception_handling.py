###############################################
#
# Exception Handling in Python
#
# An exception is an event that occurs during the execution of a program that disrupts the normal flow of instructions.
# When a Python script encounters a situation that it cannot cope with, it raises an exception.
# Keywords used for handling these include: try, except, and raise.
#
############################################### 

###############################################
#
# Exception handling during file access
#
# We put the risky code (like opening a file) inside a 'try' block.
#
############################################### 

try:
    # We are deliberately trying to open a file in read mode ('r') that does not exist
    fh = open("missing_file.txt", "r")
    data = fh.read()
    print(data)

###############################################
#
# Catching specific errors with except
#
# If the file cannot be found or read, Python raises an IOError.
# Instead of crashing, the script jumps to this 'except' block.
#
############################################### 

except IOError:
    print("Error: can't find file or read data")

###############################################
#
# Using the else block
#
# The else block will run ONLY if no exception was raised during the try block.
# If the file was successfully opened, this is where we would close it.
#
############################################### 

else:
    print("Read content from the file successfully")
    fh.close()
