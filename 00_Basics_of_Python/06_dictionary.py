###############################################
#
# Working with Dictionaries in Python
#
# A dictionary acts like an associative array in SV.
# The index and data type can be different for each entry.
#
############################################### 

# Declaring an empty dictionary and assigning values on each element basis
institute = {}
institute['name'] = 'vlsi'
institute['location'] = "BLR"
institute[1] = 'training'

# Assigning values to a complete Dictionary at once
age = { 'amit': '29', 'john': '28', 'bob': '30'}

print("Institute Dictionary:", institute,"\n")

###############################################
#
# Accessing Values in a Dictionary
#
# You can print a specific element using its key, or print all keys/values using built-in methods.
#
############################################### 

print("Name of institute:", institute['name'],"\n")
print("All keys in institute:", institute.keys(),"\n")
print("All values in institute:", institute.values(),"\n")

###############################################
#
# Updating a Dictionary
#
# You can add a new entry or modify an existing entry by referencing its key.
#
############################################### 

dict1 = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}

# Adding a new entry
dict1['place'] = "BLR"

# Modifying the existing entry
dict1['Age'] = 8

print("dict1 after updates:", dict1,"\n")

###############################################
#
# Deleting Dictionary Elements
#
# You can remove individual entries, clear all entries, or delete the entire dictionary object.
#
############################################### 

# Delete a specific element
del dict1['Name']
print("dict1 after deleting 'Name':", dict1,"\n")

# Remove all entries of dict (Dictionary exists, but it will be empty)
dict1.clear()
print("dict1 after clear():", dict1,"\n")

# Delete the entire dictionary (Dictionary will not exist anymore)
del dict1
# print(dict1) # This would now cause an error because dict1 is deleted

###############################################
#
# Advanced Dictionary Methods
#
############################################### 

advanced_dict = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}

# get(): Returns value or default if key is not in dictionary (prevents errors)
print("Get 'Age':", advanced_dict.get('Age'))
print("Get 'Location' (doesn't exist):", advanced_dict.get('Location', 'Not Found'))

# items(): Returns a list of the dictionary's (key, value) tuple pairs
print("Dictionary items:", advanced_dict.items())

# values(): Returns a list of the dictionary's values
print("Dictionary values:", advanced_dict.values())

# copy(): Returns a shallow copy of dictionary
dict_copy = advanced_dict.copy()

# update(): Adds another dictionary's key-value pairs to the current one
new_data = {'Location': 'BLR', 'Score': 95}
advanced_dict.update(new_data)
print("Dictionary after update:", advanced_dict)
