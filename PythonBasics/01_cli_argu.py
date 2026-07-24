###############################################
#
# We import sys lib to work with arguments
#
############################################### 

import sys
###############################################
#
# Assume this script is executed via terminal as: 
# len() calculates the total number of arguments
#
############################################### 

total_args = len(sys.argv)
print("Total arguments passed:", total_args)

###############################################
#
# Passing arg on run 
#
############################################### 

arg = input("Enter 'hi':")

###############################################
#
# Iterating through the list to match keywords
#
############################################### 

if arg == "hi":
    print("""Hi "I am Venkata Naga Sai!"\n""")

for arg in sys.argv:
    if arg == "hey":
        print("""Hi!!"\n""")

for arg in sys.argv:
    if arg == "bye":
        print("""bye!!"\n""")
