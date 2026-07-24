###############################################
#
# Working with Lists in Python
#
# A list contains items separated by commas and enclosed within [].
# All the items of a list can be of different data types.
#
############################################### 

# Defining lists
list1 = ['physics', 'chemistry', 1997, 2000]
list2 = [1, 2, 3, 4, 5, 6, 7]

print("Original list1:", list1)

###############################################
#
# Accessing Values in Lists
#
# The values stored in a list can be accessed using the slice operator [] and [:].
# Offsets start at zero.
#
############################################### 

print("list1[0]: ", list1[0]) 
# Slicing fetches sections. list2[1:5] will not print the 5th index.
print("list2[1:5]: ", list2[1:5]) 

###############################################
#
# Updating and Deleting Lists
#
# We can update existing values using the index.
# The del statement is used to delete one element or the complete list.
#
############################################### 

# Updating existing value
list1[2] = 2001
print("list1 after update:", list1)

# Delete List element at index 3
del list1[3]
print("list1 after deletion:", list1)

###############################################
#
# Basic List Operations
#
# + : concatenation operator (concatenates both list elements into a single list).
# * : Repetition operator.
# len() : Length of List.
#
############################################### 

list3 = ['blue', 'green', 'red']
list4 = ['yellow', 'white', 'black']

# Concatenation
complete_list = list3 + list4
print("complete_list:", complete_list)

# Length
list_size = len(complete_list)
print("list_size =", list_size)

###############################################
#
# List Methods
#
# list.append(var) appends var to the list.
# list.insert(index, obj) inserts obj into the list at offset index.
# list.pop() removes and returns the value at the specified index, last index by default.
#
############################################### 

# Append
list3.append('pink')
print("list3 after append:", list3)

# Insert 200 at index 1
list3.insert(1, 200)
print("list3 after insert:", list3)

# Pop the last element
val = list3.pop()
print("Popped value:", val)
print("list3 after pop:", list3)

###############################################
#
# Advanced Built-in List Functions and Methods
#
############################################### 

advanced_list = [10, 50, 20, 40, 30]

# Built-in functions
print("Maximum value:", max(advanced_list))
print("Minimum value:", min(advanced_list))

# List Methods
# count(): Returns count of how many times a variable occurs.
advanced_list.append(20)
print("Count of 20:", advanced_list.count(20))

# index(): Returns the lowest index where the object appears.
print("Index of 50:", advanced_list.index(50))

# remove(): Removes the object from the list.
advanced_list.remove(40)
print("After removing 40:", advanced_list)

# reverse(): Reverses the objects of the list in place.
advanced_list.reverse()
print("Reversed list:", advanced_list)

# sort(): Sorts objects of list.
advanced_list.sort()
print("Sorted list:", advanced_list)

# extend(): Appends the contents of a sequence to the list.
advanced_list.extend([100, 200])
print("Extended list:", advanced_list)
