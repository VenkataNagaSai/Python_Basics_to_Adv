import re
# Parentheses () capture groups of data within a match.
line = "Cats are smarter than dogs"
match_obj = re.match(r'(.*) are (.*?) .*', line)
if match_obj:
    print("Group 1:", match_obj.group(1))
    print("Group 2:", match_obj.group(2))
