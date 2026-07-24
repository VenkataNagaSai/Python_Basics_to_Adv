
###############################################
#
# We will be understanding import and from
#
############################################### 

import os
from datetime import datetime

# os.system("touch output.txt") - Python creates the file automatically! when we are using append if "r or +" we need to create the file if its not there

file = open("output.txt", "a+")

data = file.read()

print(f"Timestamp :{datetime.now()}\n\n",data)

# IMPROVED: Added seek(0) to move the cursor to the beginning before reading
file.seek(0)
data = file.read()

print(f"Timestamp :{datetime.now()}\n\n",data)

file.close()
