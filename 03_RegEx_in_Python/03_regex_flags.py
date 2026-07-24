import re

###############################################
#
# 1. re.I (Ignore Case)
#
############################################### 

# re.I modifies the search to ignore uppercase and lowercase differences.
line1 = "cats are smarter than dogs"
match_obj_i = re.match(r'CATS', line1, re.I)

print("--- Testing re.I (Ignore Case) ---")
if match_obj_i:
    print("Found with case ignored:", match_obj_i.group())


###############################################
#
# 2. re.M (Multi-line)
#
############################################### 

# re.M affects how '^' (start of line) and '$' (end of line) behave. 
# It makes them match the start and end of EACH LINE within a multi-line string.

multi_line_log = """Warning: Unused variable
Error: Syntax error on line 42
Warning: Timing violation
Error: Port mapping mismatch"""

print("\n--- Testing re.M (Multi-line) ---")

# We want to extract only the actual error messages from lines that START with "Error:"
# Without re.M, '^' would only check the very first line ("Warning: Unused...").
# With re.M, '^' checks the start of every single line in the block of text.

# Using re.findall to grab all matches in the multi-line string
errors = re.findall(r'^Error:\s*(.*)', multi_line_log, re.M)

print("Extracted Errors:")
for err in errors:
    print(err)
