###############################################
#
# Working with Loops in Python
#
# Python provides various types of loops such as while, for, and nested loops.
#
############################################### 

###############################################
#
# The 'while' Loop
#
# A while loop repeatedly executes a statement or statements as long as an expression is true.
# Python also supports a 'while else' construct.
#
############################################### 

count = 1
while count <= 3:
    print("While loop iteration:", count,"\n")
    count += 1
else:
    print("While loop finished gracefully.","\n")

###############################################
#
# The 'for' Loop
#
# A for loop input can be a list or a string.
# It iterates over elements of the list or characters of the string.
#
############################################### 

# Iterating over characters of a string
for letter in 'Python': 
    print('Current Letter:', letter,"\n")

# Iterating over elements of a list
fruits = ['banana', 'apple', 'mango']
for fruit in fruits: 
    print('Current fruit:', fruit,"\n")

###############################################
#
# Loop Control Statements: break, continue, and pass
#
# break: Terminates the loop statement and transfers execution to the statement immediately following the loop.
# continue: Causes the loop to skip the remainder of its body and immediately retest its condition prior to reiterating.
# pass: Used when a statement is required syntactically but you do not want any command or code to execute.
#
############################################### 

print("\nTesting loop control statements:","\n")
for i in range(1, 10, 1):
    if i == 5:
        # Using break to come out of the loop
        print("Breaking loop at i = 5","\n")
        break
    
    if i % 2 == 0:
        # Continue in the loop, only skip the remaining part of current iteration
        continue
        
    if i == 3:
        # Syntactic placeholder
        pass
        
    print("Loop control iteration:", i,"\n")

###############################################
#
# Nested Loops
#
# Loops inside loops is called as nested loops.
#
############################################### 

print("\nTesting nested loops:","\n")
for i in range(2):
    for j in range(3):
        print(f"Nested loop variables -> i: {i}, j: {j}","\n")


