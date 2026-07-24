###############################################
#
# Working with OS Module for Directories and Files
#
# The 'os' module provides system-level file and directory management.
#
############################################### 

import os

###############################################
#
# Directory Operations
#
# mkdir(): Creates a new directory.
# getcwd(): Gets the current working directory.
# chdir(): Changes the current working directory.
# rmdir(): Removes a directory.
#
############################################### 

# Print the current working directory
current_dir = os.getcwd()
print("Current Directory:", current_dir)

# Create a new directory
dir_name = "test_directory"
if not os.path.exists(dir_name):
    os.mkdir(dir_name)
    print(f"Created directory: {dir_name}")

# Change into the new directory and print it
os.chdir(dir_name)
print("Changed Directory to:", os.getcwd())

# Change back to the original directory and remove the test directory
os.chdir(current_dir)
os.rmdir(dir_name)
print(f"Removed directory: {dir_name}\n")

###############################################
#
# File Operations: Rename and Remove
#
############################################### 

# Create a dummy file to test with
with open("temp_file.txt", "w") as f:
    f.write("Just some temporary data.")

# rename(): Renames the file.
# Syntax: os.rename(current_file_name, new_file_name).
os.rename("temp_file.txt", "renamed_file.txt")
print("File 'temp_file.txt' has been renamed to 'renamed_file.txt'.")

# remove(): Deletes the file.
os.remove("renamed_file.txt")
print("File 'renamed_file.txt' has been deleted.\n")

###############################################
#
# File Operations: Replace Text in File
#
# Note: The 'os' module doesn't edit file contents directly.
# To replace text, you must read the file, replace the string, 
# and write the content back.
#
############################################### 

# Create a file with some text
with open("replace_test.txt", "w") as f:
    f.write("Hello World! This is a test file.")

print("Original content:")
with open("replace_test.txt", "r") as f:
    print(f.read())

# Read in the file
with open("replace_test.txt", "r") as file:
    file_data = file.read()

# Replace the target string
file_data = file_data.replace("World", "Python")

# Write the file out again
with open("replace_test.txt", "w") as file:
    file.write(file_data)

print("\nUpdated content:")
with open("replace_test.txt", "r") as f:
    print(f.read())

# Clean up
os.remove("replace_test.txt")
