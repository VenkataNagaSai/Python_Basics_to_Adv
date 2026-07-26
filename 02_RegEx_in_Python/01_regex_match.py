import re
# re.match() ONLY checks for a match at the VERY BEGINNING of a string.
line = "Cats are smarter than dogs"
match_obj = re.match(r'Cat', line)
if match_obj:
    print("re.match found:", match_obj.group())
