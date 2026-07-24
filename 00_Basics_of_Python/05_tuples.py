###############################################
#
# Working with Tuples in Python
#
# A Tuple stores a list of values, but unlike lists, they can't be changed (they are read-only lists).
# Tuples are typically enclosed within parentheses () and their items are separated by commas.
#
############################################### 

# Defining tuples
tup1 = ('physics', 'chemistry', 1997, 2000)
tup2 = (1, 2, 3, 4, 5)

print("Original tup1:", tup1)

###############################################
#
# Accessing Values in Tuples
#
# You can access elements using indices and slicing, exactly like you do with lists.
#
############################################### 

print("tup1[0]: ", tup1[0])

# This prints elements from index 1 up to (but not including) index 5
print("tup2[1:5]: ", tup2[1:5]) 

###############################################
#
# Updating and Deleting Tuples
#
# Tuples are immutable which means you cannot update or change the values of tuple elements.
# Removing individual tuple elements is also not possible.
# However, you can create a new tuple by concatenating existing ones.
#
############################################### 

# tup1[0] = 100  # NOTE: This is not valid and will throw an error because tuples are immutable.

# Creating a new tuple via concatenation
tup3 = tup1 + tup2
print("tup3 (after concatenation):", tup3)

###############################################
#
# Tuple Operations and Built-in Functions
#
# Basic operations like len() for length, + for concatenation, and * for repetition work on tuples.
# Python also provides built-in functions like max(), min(), and tuple() to convert a list into a tuple.
#
############################################### 

# Length of a tuple
print("Length of tup3:", len(tup3))

# Repetition operation
tup4 = (1, 2, 3)
print("Repetition (tup4 * 2):", tup4 * 2)

# Converting a list into a tuple using the tuple(seq) method
sample_list = ['red', 'green', 'blue']
converted_tuple = tuple(sample_list)
print("Converted tuple from list:", converted_tuple)

###############################################
#
# Advanced Tuple Functions
#
# Built-in functions specifically used for tuples.
#
############################################### 

num_tuple = (15, 30, 45, 10, 60)

# max() and min() return the maximum and minimum values in the tuple
print("Maximum value in tuple:", max(num_tuple))
print("Minimum value in tuple:", min(num_tuple))
