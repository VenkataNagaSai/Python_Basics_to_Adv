###############################################
#
# Working with Strings
#
# A string is a contiguous set of characters represented in quotation marks.
# Python accepts single ('), double ("), and triple (''' or """) quotes.
#
############################################### 

str_val = 'Hello World!'
print(str_val)
###############################################
#
# Slicing, Concatenation, and Repetition
#
# You can access parts of a string using slicing, similar to lists.
# + is used for concatenation, and * is used for repetition.
#
############################################### 

print("First character:", str_val[0])
print("Characters 3rd to 5th:", str_val[2:5])
print("String two times:", str_val * 2)
print("Concatenated string:", str_val + " TEST")

###############################################
#
# String Methods
#
# Python strings are immutable, so methods output a new string.
# strip(): Removes leading and trailing whitespaces.
# replace(): Replaces a string pattern with a new pattern.
# split() and join(): Used to split a string into a list and join a list into a string.
#
############################################### 

test_str = "   I am learning Python   "
print("Original:", test_str)
print("Stripped:", test_str.strip())

# Replacing text
print("Replaced:", test_str.replace("Python", "VHDL"))

# Splitting and joining (often used to get rid of duplicate spaces)
words_list = test_str.split()
joined_str = " ".join(words_list)
print("Split and Joined:", joined_str)

###############################################
#
# Type Conversion
#
# Allows data type conversions using functions like str() and int().
#
############################################### 

num1 = '10'
num2 = '20'

# Converting strings to integers for addition
result = int(num1) + int(num2)
print("Converted to int and added:", result)

# Converting an integer back to a string
print("Converted back to string:", str(result) + " is the answer")
