################################################
##
## Working with Functions in Python
##
## A function is a group of related statements that perform a specific task.
## There are 2 types of functions: Built in and User defined.
##
################################################ 
#
################################################
##
## Defining a Function and Local Scope
##
## Parameters and variables defined inside a function are not visible from outside. 
## Hence, they have a local scope.
##
################################################ 
#
#def my_func():
#    """docstring"""
#    x = 10
#    print("Value inside function:", x,"\n")
#
#x = 20
#my_func()
#print("Value outside function:", x,"\n")
#
################################################
##
## Passing Arguments to a Function
##
## You can pass arguments (like list elements) to a function and return a calculated value.
##
################################################ 

def sum(a, b):
    return a + b

list1 = [1, 2, 3, 4, 5]
list2 = [10, 20, 30, 40, 50]
list3 = []

# Iterating and passing arguments from lists to the sum function
for i in range(0, len(list1), 1):
    list3.append(sum(list1[i], list2[i]))

print("Resulting list3 after sum function:", list3,"\n")
