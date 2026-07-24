###############################################
#
# Python Operators
#
# Python provides several categories of operators to perform mathematical, logical, and comparative operations.
#
############################################### 

a = 10
b = 3

###############################################
#
# Arithmetic and Assignment Operators
#
# Arithmetic operators include: +, -, *, /, %, **, //.
# Assignment operators include: =, +=, -=, *=, /=, %=, **=, //=.
#
############################################### 

# Arithmetic operations
print("Addition (a + b):", a + b,"\n")
print("Exponentiation (a ** b):", a ** b,"\n")
print("Floor Division (a // b):", a // b,"\n")

# Assignment operations
c = 5
c += a  # Equivalent to c = c + a
print("Value of c after += operator:", c,"\n")

###############################################
#
# Comparison and Logical Operators
#
# Comparison operators: <, >, <=, >=, <>.
# Logical Operators: and, or, not.
#
############################################### 

# Comparison
print("Is a greater than b?", a > b,"\n")

# Logical
print("Logical AND (a > 5 and b < 5):", a > 5 and b < 5,"\n")
print("Logical NOT (not(a == 10)):", not(a == 10,),"\n")

###############################################
#
# Membership and Identity Operators
#
# Membership operators (in, not in) are used to test whether a value is a member of a sequence.
# Identity operators (is, is not) compare the memory locations of two objects to see if id(x) equals id(y).
#
############################################### 

# Membership
sample_list = [1, 2, 3, 4, 5]
print("Is 3 in sample_list?", 3 in sample_list,"\n")

# Identity
x = 20
y = 20
print("Does x have the same identity as y (x is y)?", x is y,"\n")

###############################################
#
# Bitwise Operators
#
# Bitwise operators are used to compare binary numbers: &, |, ~, ^, <<, >>.
#
############################################### 

# Bitwise AND
print("Bitwise AND of a and b (a & b:", a & b,"\n")
