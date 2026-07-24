###############################################
#
# Conditional Statements
#
# Conditional statements in Python include if, if else, and if elif elif else...
#
############################################### 

var = 100

###############################################
#
# Single Line 'if' Statement
#
# You can write an if statement on a single line. 
# Example provided in the material: if (var==100): print "Value of expression is 100".
#
############################################### 

if (var == 100): print("Value of expression is 100\n")
print("value is not 100\n")

###############################################
#
# Using if, elif, and else block
#
# The structure evaluates expression1, then expression2, then expression3, and falls back to else if none match.
#
############################################### 

expression_value = 50

if expression_value == 10:
    print("Executing statement(s) for expression 1\n")
elif expression_value == 20:
    print("Executing statement(s) for expression 2\n")
elif expression_value == 50:
    print("Executing statement(s) for expression 3\n")
else:
    print("Executing statement(s) for else condition\n")
